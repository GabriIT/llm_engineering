from __future__ import annotations

import argparse
import os
import time
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from myRAG_app.api.schemas import (
    HealthResponse,
    QueryMeta,
    QueryRequest,
    QueryResponse,
    RetrievalOptions,
    SourceRef,
    StructuredAnswer,
)
from myRAG_app.api.thread_memory import create_thread_memory_store_from_env
from myRAG_app.vector.answer import answer_question_structured
from myRAG_app.vector.config import (
    DEFAULT_CHAT_MODEL,
    DEFAULT_COLLECTION_NAME,
    DEFAULT_DB_PATH,
    DEFAULT_EMBEDDING_MODEL,
)


DEFAULT_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


def _allowed_origins_from_env() -> list[str]:
    raw = os.getenv("MYRAG_ALLOWED_ORIGINS", "")
    if not raw.strip():
        return DEFAULT_ALLOWED_ORIGINS
    origins = [item.strip() for item in raw.split(",") if item.strip()]
    return origins or DEFAULT_ALLOWED_ORIGINS


def create_app() -> FastAPI:
    app = FastAPI(title="myRAG API", version="0.1.0")
    allowed_origins = _allowed_origins_from_env()
    thread_memory_store = create_thread_memory_store_from_env()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/api/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        db_path = Path(os.getenv("MYRAG_DB_PATH", str(DEFAULT_DB_PATH))).expanduser().resolve()
        collection = os.getenv("MYRAG_COLLECTION", DEFAULT_COLLECTION_NAME)
        memory_health = thread_memory_store.health()
        return HealthResponse(
            status="ok",
            collection=collection,
            db_path=str(db_path),
            thread_memory_enabled=bool(memory_health.get("enabled", False)),
            thread_memory_ready=bool(memory_health.get("ready", False)),
            threads_db=memory_health.get("db_name"),
            thread_memory_error=memory_health.get("last_error"),
        )

    @app.post("/api/rag/query", response_model=QueryResponse)
    def query_rag(payload: QueryRequest) -> QueryResponse:
        started = time.perf_counter()
        retrieval = payload.retrieval or RetrievalOptions()

        client_history = [{"role": item.role, "content": item.content} for item in payload.history]
        thread_memory_used = False
        thread_memory_ready: bool | None = None
        history = client_history
        username = (payload.username or "").strip()
        thread_id = (payload.thread_id or "").strip()

        if username and thread_id and thread_memory_store.enabled:
            memory_health = thread_memory_store.health()
            thread_memory_ready = bool(memory_health.get("ready", False))
            if thread_memory_ready:
                history = thread_memory_store.build_history(
                    username=username,
                    thread_id=thread_id,
                    question=payload.question,
                    fallback_history=client_history,
                )
                thread_memory_used = True

        selected_chat_model = payload.chat_model or DEFAULT_CHAT_MODEL

        db_path = Path(os.getenv("MYRAG_DB_PATH", str(DEFAULT_DB_PATH))).expanduser().resolve()
        collection = os.getenv("MYRAG_COLLECTION", DEFAULT_COLLECTION_NAME)

        try:
            structured_answer, answer, docs = answer_question_structured(
                payload.question,
                history=history,
                db_path=db_path,
                collection_name=collection,
                embedding_model=DEFAULT_EMBEDDING_MODEL,
                chat_model=selected_chat_model,
                k=retrieval.k,
                search_type=retrieval.search_type,
                fetch_k=retrieval.fetch_k,
                lambda_mult=retrieval.lambda_mult,
                doc_type=retrieval.doc_type,
                source_contains=retrieval.source_contains,
            )
        except Exception as exc:
            raise HTTPException(
                status_code=500,
                detail={
                    "error": "backend_error",
                    "message": str(exc),
                },
            ) from exc

        if thread_memory_used:
            assistant_metadata = {
                "chat_model": selected_chat_model,
                "structured": {
                    "prompt": structured_answer.prompt,
                    "bullets": structured_answer.bullets,
                    "answer_text": structured_answer.answer_text,
                },
                "sources": [
                    {
                        "source": str((doc.metadata or {}).get("source", "unknown")),
                        "source_name": str((doc.metadata or {}).get("source_name", "unknown")),
                        "doc_type": str((doc.metadata or {}).get("doc_type", "unknown")),
                        "page_number": (doc.metadata or {}).get("page_number"),
                        "sheet_name": (doc.metadata or {}).get("sheet_name"),
                    }
                    for doc in docs[:20]
                ],
            }
            thread_memory_store.persist_turn(
                username=username,
                thread_id=thread_id,
                question=payload.question,
                answer=answer,
                assistant_metadata=assistant_metadata,
            )

        seen = set()
        sources: list[SourceRef] = []
        for doc in docs:
            metadata = doc.metadata or {}
            source_ref = SourceRef(
                source=str(metadata.get("source", "unknown")),
                source_name=str(metadata.get("source_name", "unknown")),
                doc_type=str(metadata.get("doc_type", "unknown")),
                page_number=metadata.get("page_number"),
                sheet_name=metadata.get("sheet_name"),
            )
            dedupe_key = (
                source_ref.source,
                source_ref.page_number,
                source_ref.sheet_name,
            )
            if dedupe_key in seen:
                continue
            seen.add(dedupe_key)
            sources.append(source_ref)

        elapsed_ms = int((time.perf_counter() - started) * 1000)
        return QueryResponse(
            answer=answer,
            structured=StructuredAnswer(
                prompt=structured_answer.prompt,
                bullets=structured_answer.bullets,
                answer_text=structured_answer.answer_text,
            ),
            sources=sources,
            meta=QueryMeta(
                chat_model=selected_chat_model,
                embedding_model=DEFAULT_EMBEDDING_MODEL,
                k=retrieval.k,
                search_type=retrieval.search_type,
                elapsed_ms=elapsed_ms,
                thread_memory_used=thread_memory_used,
                thread_memory_ready=thread_memory_ready,
                thread_id=thread_id or None,
            ),
        )

    return app


app = create_app()


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run myRAG FastAPI server.")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host (default: 0.0.0.0).")
    parser.add_argument("--port", type=int, default=8000, help="Bind port (default: 8000).")
    parser.add_argument("--reload", action="store_true", help="Enable autoreload for development.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    uvicorn.run("myRAG_app.api.server:app", host=args.host, port=args.port, reload=args.reload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
