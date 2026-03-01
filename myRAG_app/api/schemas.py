from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, field_validator

from myRAG_app.vector.config import (
    DEFAULT_CHAT_MODEL,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_RETRIEVAL_FETCH_K,
    DEFAULT_RETRIEVAL_K,
    DEFAULT_RETRIEVAL_LAMBDA_MULT,
    DEFAULT_RETRIEVAL_SEARCH_TYPE,
)

RoleType = Literal["user", "assistant"]
SearchType = Literal["similarity", "mmr"]


class HistoryMessage(BaseModel):
    role: RoleType
    content: str = Field(..., min_length=1)

    @field_validator("content")
    @classmethod
    def validate_content(cls, value: str) -> str:
        content = value.strip()
        if not content:
            raise ValueError("content must not be blank")
        return content


class RetrievalOptions(BaseModel):
    k: int = Field(default=DEFAULT_RETRIEVAL_K, ge=1, le=50)
    search_type: SearchType = DEFAULT_RETRIEVAL_SEARCH_TYPE
    fetch_k: int = Field(default=DEFAULT_RETRIEVAL_FETCH_K, ge=1, le=200)
    lambda_mult: float = Field(default=DEFAULT_RETRIEVAL_LAMBDA_MULT, ge=0.0, le=1.0)
    doc_type: str | None = None
    source_contains: str | None = None


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1)
    history: list[HistoryMessage] = Field(default_factory=list)
    retrieval: RetrievalOptions | None = None

    @field_validator("question")
    @classmethod
    def validate_question(cls, value: str) -> str:
        question = value.strip()
        if not question:
            raise ValueError("question must not be blank")
        return question


class SourceRef(BaseModel):
    source: str
    source_name: str
    doc_type: str
    page_number: int | None = None
    sheet_name: str | None = None


class QueryMeta(BaseModel):
    chat_model: str = DEFAULT_CHAT_MODEL
    embedding_model: str = DEFAULT_EMBEDDING_MODEL
    k: int
    search_type: SearchType
    elapsed_ms: int


class QueryResponse(BaseModel):
    answer: str
    sources: list[SourceRef]
    meta: QueryMeta


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    collection: str
    db_path: str
