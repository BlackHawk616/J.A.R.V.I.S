"""Persistent vector-DB memory for JARVIS.

Stores facts as concise bullet points in a local ChromaDB collection.
Uses sentence-transformers (all-MiniLM-L6-v2) for offline embeddings
and LangChain-Chroma for the retrieval pipeline.

Usage:
    from memory import init_memory, add_memory, search_memory, get_memory_context

    init_memory()                        # call once at startup
    add_memory("User's name is Charan")  # store a fact
    ctx = get_memory_context("what is my name?")  # retrieve relevant memories
"""

from __future__ import annotations

import datetime
import os
from pathlib import Path
from typing import Optional

# ── Paths ───────────────────────────────────────────────────────────
_PROJECT_DIR = Path(__file__).resolve().parent
_DB_DIR = str(_PROJECT_DIR / "database" / "memory_store")

# ── Tunables via env vars ───────────────────────────────────────────
_COLLECTION_NAME = os.getenv("JARVIS_MEMORY_COLLECTION", "jarvis_memory")
_EMBEDDING_MODEL = os.getenv("JARVIS_MEMORY_EMBED_MODEL", "all-MiniLM-L6-v2")
_DEFAULT_K = int(os.getenv("JARVIS_MEMORY_TOP_K", "3"))

# ── Module-level singletons (populated by init_memory) ──────────────
_vectorstore = None
_is_initialized = False


def init_memory() -> None:
    """Initialize the ChromaDB vector store and embedding model.

    Safe to call multiple times — only initializes once.
    """
    global _vectorstore, _is_initialized
    if _is_initialized:
        return

    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_chroma import Chroma

    # Ensure the storage directory exists
    os.makedirs(_DB_DIR, exist_ok=True)

    embeddings = HuggingFaceEmbeddings(
        model_name=_EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )

    _vectorstore = Chroma(
        collection_name=_COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=_DB_DIR,
    )

    _is_initialized = True
    count = _vectorstore._collection.count()
    print(f"[Memory] Loaded {count} memories from {_DB_DIR}")


def _today() -> str:
    return datetime.date.today().isoformat()


def add_memory(text: str) -> str:
    """Store a fact as a concise bullet point in the vector DB.

    Args:
        text: The raw text to remember.

    Returns:
        The formatted bullet-point string that was stored.
    """
    if not _is_initialized or _vectorstore is None:
        init_memory()

    # Clean up and format as a bullet point
    cleaned = text.strip().rstrip(".")
    bullet = f"• {cleaned} ({_today()})"

    _vectorstore.add_texts(
        texts=[bullet],
        metadatas=[{"date": _today(), "raw": text.strip()}],
    )

    print(f"[Memory] Stored: {bullet}")
    return bullet


def search_memory(query: str, k: Optional[int] = None) -> list[str]:
    """Search for the top-k most relevant memories.

    Args:
        query: The search query.
        k: Number of results to return (default: JARVIS_MEMORY_TOP_K or 3).

    Returns:
        List of bullet-point memory strings, most relevant first.
    """
    if not _is_initialized or _vectorstore is None:
        init_memory()

    k = k or _DEFAULT_K
    count = _vectorstore._collection.count()
    if count == 0:
        return []

    # Don't request more results than we have
    effective_k = min(k, count)
    results = _vectorstore.similarity_search(query, k=effective_k)
    return [doc.page_content for doc in results]


def get_memory_context(query: str, k: Optional[int] = None) -> str:
    """Get a formatted memory context string for injection into the AI prompt.

    Args:
        query: The user's question.
        k: Number of memories to retrieve.

    Returns:
        A formatted string with relevant memories, or empty string if none.
    """
    memories = search_memory(query, k)
    if not memories:
        return ""

    lines = "\n".join(memories)
    return (
        f"Here are relevant things you remember about the user:\n"
        f"{lines}\n"
        f"Use these memories to give personalized answers when relevant."
    )


def get_all_memories() -> list[str]:
    """Return all stored memories (for review / debugging).

    Returns:
        List of all bullet-point memory strings.
    """
    if not _is_initialized or _vectorstore is None:
        init_memory()

    count = _vectorstore._collection.count()
    if count == 0:
        return []

    results = _vectorstore._collection.get()
    documents = results.get("documents", [])
    return documents if documents else []


def extract_remember_payload(query: str) -> str:
    """Extract the core fact to remember from a query containing the word 'remember'.

    Examples:
        "your name is jarvis remember it" -> "your name is jarvis"
        "remember that my keys are on the desk" -> "my keys are on the desk"
        "remember to buy milk" -> "buy milk"
        "remember" -> "" (empty, meaning ask user what to remember)
    """
    query = query.strip()
    
    # Check if the query is just a remember command without payload
    normalized = query.lower().rstrip("!?.")
    if normalized in ["remember", "remember this", "remember that", "remember it"]:
        return ""

    # Strip common prefixes
    prefixes = ["remember that ", "remember this ", "remember to ", "remember "]
    for prefix in prefixes:
        if normalized.startswith(prefix):
            query = query[len(prefix):].strip()
            # Re-normalize to strip further prefixes if any
            normalized = query.lower()
            break

    # Strip common suffixes
    suffixes = [
        " remember it",
        " remember this",
        " remember that",
        " remember",
        " please remember",
        ", remember it",
        ", remember this",
    ]
    for suffix in suffixes:
        if normalized.endswith(suffix):
            query = query[:-len(suffix)].strip()
            break

    return query.strip().rstrip("!?.")
