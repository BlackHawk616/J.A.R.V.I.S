"""Fallback AI client for JARVIS.

Supports running a small local model (Qwen2.5-0.5B-Instruct) offline,
or falling back to the cloud-based NVIDIA NIM (MiniMax M3).
"""

from __future__ import annotations

import os
import threading
import time
from collections import deque
from dataclasses import dataclass
from typing import Optional

from openai import OpenAI

# ── Tunables via env vars ───────────────────────────────────────────
_LLM_MODE = os.getenv("JARVIS_LLM_MODE", "local").lower()  # "local" or "nim"
_LOCAL_MODEL_NAME = os.getenv("JARVIS_LOCAL_MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
_NIM_MODEL_NAME = os.getenv("JARVIS_NIM_MODEL", "minimaxai/minimax-m3")

# ── Eager Load singletons for Local LLM ─────────────────────────────
_local_model = None
_local_tokenizer = None
_local_lock = threading.Lock()
_local_initialized = False


def init_local_llm() -> None:
    """Initialize the local Qwen LLM and tokenizer.

    Safe to call multiple times or from a thread.
    """
    global _local_model, _local_tokenizer, _local_initialized
    if _local_initialized:
        return

    with _local_lock:
        if _local_initialized:
            return

        try:
            print(f"[LLM] Eagerly loading local model: {_LOCAL_MODEL_NAME}...")
            start = time.time()
            from transformers import AutoModelForCausalLM, AutoTokenizer

            _local_tokenizer = AutoTokenizer.from_pretrained(_LOCAL_MODEL_NAME)
            _local_model = AutoModelForCausalLM.from_pretrained(_LOCAL_MODEL_NAME)
            _local_initialized = True
            print(f"[LLM] Local model loaded in {time.time() - start:.2f}s")
        except Exception as e:
            print(f"[LLM] Warning: Failed to load local model: {e}")


# Start eager loading of the local LLM in a background thread
if _LLM_MODE == "local":
    threading.Thread(target=init_local_llm, daemon=True).start()


# ── Cloud NIM Rate Limiter ──────────────────────────────────────────
@dataclass
class _RateConfig:
    # Increased token and request limits so embedding queries do not trigger the rate limiter
    requests_per_minute: int = int(os.getenv("JARVIS_NIM_REQUESTS_PER_MIN", "60"))
    tokens_per_minute: int = int(os.getenv("JARVIS_NIM_TOKENS_PER_MIN", "100000"))
    max_response_tokens: int = int(os.getenv("JARVIS_NIM_MAX_OUTPUT_TOKENS", "500"))


class _StrongRateLimiter:
    def __init__(self, config: _RateConfig) -> None:
        self.config = config
        self._request_times: deque[float] = deque()
        self._token_events: deque[tuple[float, int]] = deque()

    def _evict_old(self, now: float) -> None:
        cutoff = now - 60.0
        while self._request_times and self._request_times[0] < cutoff:
            self._request_times.popleft()
        while self._token_events and self._token_events[0][0] < cutoff:
            self._token_events.popleft()

    def _approx_tokens(self, text: str) -> int:
        return max(1, len(text) // 4)

    def allow(self, user_text: str) -> tuple[bool, str]:
        now = time.time()
        self._evict_old(now)

        if len(self._request_times) >= self.config.requests_per_minute:
            return (
                False,
                "Rate limit reached. Please wait a bit before asking another open-ended question.",
            )

        input_tokens = self._approx_tokens(user_text)
        used_tokens = sum(tokens for _, tokens in self._token_events)
        projected = used_tokens + input_tokens + self.config.max_response_tokens
        if projected > self.config.tokens_per_minute:
            return (
                False,
                "Token budget limit reached for this minute. Please retry shortly.",
            )

        self._request_times.append(now)
        self._token_events.append((now, input_tokens + self.config.max_response_tokens))
        return True, ""


_SYSTEM_PROMPT = (
    "You are JARVIS, a concise and practical AI assistant for desktop automation. "
    "Prefer short, clear answers in plain text. Avoid markdown decoration and asterisks."
)

_rate_limiter = _StrongRateLimiter(_RateConfig())


def _get_client() -> OpenAI:
    api_key = "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"
    if not api_key:
        raise RuntimeError("Missing NVIDIA_API_KEY environment variable.")

    return OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key,
        timeout=15.0,  # Don't hang JARVIS if the API is slow
    )


def _get_local_response(user_query: str, system_prompt: str) -> str:
    """Generate a response using the locally cached Qwen model."""
    if not _local_initialized:
        # Try to initialize synchronously if not ready
        init_local_llm()

    if not _local_initialized or _local_model is None or _local_tokenizer is None:
        raise RuntimeError("Local LLM model is not loaded.")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ]

    text = _local_tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    model_inputs = _local_tokenizer([text], return_tensors="pt").to(_local_model.device)

    generated_ids = _local_model.generate(
        **model_inputs,
        max_new_tokens=250,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )
    generated_ids = [
        output_ids[len(input_ids) :]
        for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = _local_tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response.strip()


def get_nim_response(user_query: str, memory_context: str = "") -> str:
    """Get a response from the fallback AI (local Qwen or cloud MiniMax NIM).

    Args:
        user_query: The user's question.
        memory_context: Optional formatted memory string to inject into the prompt.
    """
    # Build system prompt, optionally enriched with memory context
    system_prompt = _SYSTEM_PROMPT
    if memory_context:
        system_prompt = f"{_SYSTEM_PROMPT}\n\n{memory_context}"

    # Try local LLM if configured
    if _LLM_MODE == "local":
        try:
            return _get_local_response(user_query, system_prompt)
        except Exception as e:
            print(f"[LLM] Local inference failed: {e}. Falling back to NIM API.")

    # Fallback to Cloud NIM API
    allowed, reason = _rate_limiter.allow(user_query)
    if not allowed:
        return reason

    try:
        client = _get_client()
        completion = client.chat.completions.create(
            model=_NIM_MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query},
            ],
            temperature=0.6,
            top_p=0.95,
            max_tokens=_rate_limiter.config.max_response_tokens,
            stream=False,
            extra_body={"chat_template_kwargs": {"thinking_mode": "disabled"}},
        )

        content = completion.choices[0].message.content or ""
        text = content.replace("*", "").strip()
        return text or "I am not sure yet, but I can try again with a clearer prompt."
    except Exception:
        return "I could not reach the fallback model right now. Please check network access."
