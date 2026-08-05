"""Shared text-to-speech engine for JARVIS.

Primary engine: KittenTTS (direct playback, no file output)
Fallback engine: pyttsx3 (platform default driver)
"""

from __future__ import annotations

import os
import re
import threading
import time
from typing import Optional

# ── Force KittenTTS to use locally-cached model files only ──────────
os.environ.setdefault("HF_HUB_OFFLINE", "1")

import numpy as np

_SAMPLE_RATE = 24000
_DEFAULT_MODEL = os.getenv("JARVIS_TTS_MODEL", "KittenML/kitten-tts-nano-0.8")
_DEFAULT_VOICE = os.getenv("JARVIS_TTS_VOICE", "Hugo")
_DEFAULT_SPEED = float(os.getenv("JARVIS_TTS_SPEED", "1.35"))
_DEFAULT_GAIN = float(os.getenv("JARVIS_TTS_GAIN", "2.0"))

_lock = threading.Lock()
_kitten_model = None
_kitten_voices: list[str] = []
_fallback_engine = None

# ── Speech State Variables ──────────────────────────────────────────
_current_speech_thread: Optional[threading.Thread] = None
_stop_requested = False
_remaining_text = ""
_saved_remaining_text = ""
_last_spoken_text = ""


def _boost_audio(audio: np.ndarray, gain: float) -> np.ndarray:
    peak = float(np.max(np.abs(audio))) if audio.size else 0.0
    if peak <= 0.0:
        return audio

    normalized = audio / peak
    boosted = normalized * min(max(gain, 0.5), 3.0)
    return np.clip(boosted, -0.98, 0.98).astype(np.float32)


def _init_kitten_model() -> None:
    global _kitten_model, _kitten_voices
    if _kitten_model is not None:
        return

    from kittentts import KittenTTS

    _kitten_model = KittenTTS(_DEFAULT_MODEL)
    _kitten_voices = list(_kitten_model.available_voices)


try:
    _init_kitten_model()
except Exception:
    pass


def _clean_for_speech(text: str) -> str:
    """Clean markdown, dashes, and extra whitespace to prevent TTS model shape crashes."""
    # Remove markdown headers and asterisks/underscores/backticks/brackets/braces
    text = re.sub(r'[*#_`~|[\]{}]', ' ', text)
    # Remove lists of dashes (like ---)
    text = re.sub(r'-{2,}', ' ', text)
    # Replace single dashes with spaces if they are not in-word hyphens
    text = re.sub(r'\s+-\s+', ' ', text)
    # Replace multiple spaces/newlines with a single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def _speak_with_fallback(text: str) -> None:
    import platform
    import subprocess

    if platform.system() == "Darwin":
        try:
            # macOS native 'say' command (bulletproof, works fully offline)
            subprocess.run(["say", text], check=True)
            return
        except Exception:
            pass

    # Secondary fallback for non-macOS or if 'say' fails
    try:
        global _fallback_engine
        if _fallback_engine is None:
            import pyttsx3

            _fallback_engine = pyttsx3.init()

        _fallback_engine.say(text)
        _fallback_engine.runAndWait()
    except Exception as e:
        print(f"[Fallback TTS Error] Could not speak text: {e}")


def _speech_worker(text: str, sentences: list[str]) -> None:
    """Worker thread target to play back multi-sentence TTS asynchronously."""
    global _stop_requested, _remaining_text, _last_spoken_text
    _stop_requested = False
    _remaining_text = text
    _last_spoken_text = text

    try:
        import sounddevice as sd
    except Exception:
        # Fallback to standard blocking engine if sounddevice is not available
        _speak_with_fallback(text)
        _remaining_text = ""
        return

    try:
        _init_kitten_model()
        selected_voice = _DEFAULT_VOICE
        if selected_voice not in _kitten_voices and _kitten_voices:
            selected_voice = _kitten_voices[0]

        for i, sentence in enumerate(sentences):
            if _stop_requested:
                break

            # Update remaining text to speak
            _remaining_text = " ".join(sentences[i:])

            # Generate audio for the sentence
            audio = _kitten_model.generate(
                sentence, voice=selected_voice, speed=_DEFAULT_SPEED
            )
            audio = np.asarray(audio, dtype=np.float32)
            audio = _boost_audio(audio, _DEFAULT_GAIN)

            if _stop_requested:
                break

            # Play the sentence
            sd.stop()
            sd.play(audio, _SAMPLE_RATE, blocking=True)

        if not _stop_requested:
            _remaining_text = ""

    except Exception:
        # Fallback if any error occurs
        if not _stop_requested:
            _speak_with_fallback(text)
            _remaining_text = ""


def speak(audio: object, blocking: bool = True) -> None:
    """Speak any value by converting it to text.

    Defaults to blocking=True so greetings, errors, and system prompts play
    completely before proceeding. Long-form responses should set blocking=False
    to run asynchronously and allow voice interruptions.
    """
    global _current_speech_thread

    # Stop any current speech before starting new speech
    stop_speaking()

    # Wait briefly for the previous thread to join/terminate
    if _current_speech_thread is not None:
        _current_speech_thread.join(timeout=0.5)

    text = str(audio).strip()
    text = _clean_for_speech(text)
    if not text:
        return

    # Split text into sentences for sentence-by-sentence play & interrupt check
    sentences = [
        s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()
    ]
    if not sentences:
        return

    _current_speech_thread = threading.Thread(
        target=_speech_worker, args=(text, sentences), daemon=True
    )
    _current_speech_thread.start()

    if blocking:
        _current_speech_thread.join()


def stop_speaking() -> None:
    """Immediately stop any active speaker output and save remaining text."""
    global _stop_requested, _saved_remaining_text, _remaining_text
    _stop_requested = True
    try:
        import sounddevice as sd

        sd.stop()
    except Exception:
        pass

    if _remaining_text:
        # Save the remainder so it can be resumed by saying "continue"
        _saved_remaining_text = _remaining_text
        _remaining_text = ""


def continue_speaking() -> bool:
    """Resume speaking the last saved remaining text from interruption.

    Returns:
        True if there was text to resume, False otherwise.
    """
    global _saved_remaining_text
    if _saved_remaining_text:
        text_to_speak = _saved_remaining_text
        _saved_remaining_text = ""  # Clear so it doesn't double-trigger
        speak(text_to_speak, blocking=False)
        return True
    return False


def is_speaking() -> bool:
    """Check if the assistant is currently speaking."""
    return (
        _current_speech_thread is not None
        and _current_speech_thread.is_alive()
    )


def should_ignore_query(query: str) -> bool:
    """Determine if a recognized query is an echo of JARVIS's own speech.

    Prevents JARVIS from self-triggering on its speaker output. Never ignores
    explicit control keywords.
    """
    if not is_speaking():
        return False

    query_clean = query.lower().strip().rstrip(".!?")
    if not query_clean:
        return True

    # Explicit control keywords must NEVER be ignored
    control_words = ["stop", "continue", "pause", "shut up", "wait"]
    if any(cw in query_clean for cw in control_words):
        return False

    # If the recognized query is a substring of the text currently being spoken
    spoken_clean = _last_spoken_text.lower()
    if query_clean in spoken_clean:
        print(f"[Echo Filter] Ignored self-talk: {query_clean!r}")
        return True

    return False
