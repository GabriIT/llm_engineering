from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_DB_PATH = Path(
    os.getenv("MYRAG_DB_PATH", str(PROJECT_ROOT / "vector_db"))
).expanduser().resolve()
DEFAULT_COLLECTION_NAME = os.getenv("MYRAG_COLLECTION", "myrag_docs")

DEFAULT_EMBEDDING_MODEL = "text-embedding-3-large"
DEFAULT_CHAT_MODEL = "gpt-4.1-nano"
OLLAMA_CHAT_MODELS = (
    "qwen3.5:9b",
    "llama3.2:latest",
)
SUPPORTED_CHAT_MODELS = (DEFAULT_CHAT_MODEL, *OLLAMA_CHAT_MODELS)

DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200
DEFAULT_RETRIEVAL_K = 8
DEFAULT_RETRIEVAL_SEARCH_TYPE = "mmr"
DEFAULT_RETRIEVAL_FETCH_K = 40
DEFAULT_RETRIEVAL_LAMBDA_MULT = 0.35
