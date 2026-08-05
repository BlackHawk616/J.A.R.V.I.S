"""KittenTTS demo: generate speech and play it directly (no file save)."""

import argparse
import sys

import sounddevice as sd
from kittentts import KittenTTS

SAMPLE_RATE = 24000
DEFAULT_MODEL = "KittenML/kitten-tts-nano-0.8"
DEFAULT_VOICE = "Luna"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate speech with KittenTTS and play audio directly."
    )
    parser.add_argument(
        "--text",
        default="Hello from JARVIS and Kitten TTS. This is direct speaker output.",
        help="Text to synthesize.",
    )
    parser.add_argument(
        "--voice",
        default=DEFAULT_VOICE,
        help="Voice name (for example: Bella, Jasper, Luna, Bruno, Rosie, Hugo, Kiki, Leo).",
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=1.0,
        help="Speech speed multiplier.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Hugging Face model id.",
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help="Print available voices and exit.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    print(f"Loading model: {args.model}")
    model = KittenTTS(args.model)

    if args.list_voices:
        print("Available voices:", ", ".join(model.available_voices))
        return 0

    if args.voice not in model.available_voices:
        print(
            f"Voice '{args.voice}' is not available. "
            f"Use one of: {', '.join(model.available_voices)}",
            file=sys.stderr,
        )
        return 1

    print(f"Synthesizing with voice={args.voice}, speed={args.speed}...")
    audio = model.generate(args.text, voice=args.voice, speed=args.speed)

    # Play generated NumPy audio directly without writing a WAV file.
    sd.play(audio, SAMPLE_RATE)
    sd.wait()
    print("Playback finished.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
