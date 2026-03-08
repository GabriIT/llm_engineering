from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator

from myRAG_app.vector.config import (
    DEFAULT_CHAT_MODEL,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_RETRIEVAL_FETCH_K,
    DEFAULT_RETRIEVAL_K,
    DEFAULT_RETRIEVAL_LAMBDA_MULT,
    DEFAULT_RETRIEVAL_SEARCH_TYPE,
    SUPPORTED_CHAT_MODELS,
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
    chat_model: str | None = None
    username: str | None = None
    thread_id: str | None = None

    @field_validator("question")
    @classmethod
    def validate_question(cls, value: str) -> str:
        question = value.strip()
        if not question:
            raise ValueError("question must not be blank")
        return question

    @field_validator("chat_model")
    @classmethod
    def validate_chat_model(cls, value: str | None) -> str | None:
        if value is None:
            return None
        model = value.strip()
        if not model:
            return None
        if model not in SUPPORTED_CHAT_MODELS:
            raise ValueError(
                f"chat_model must be one of: {', '.join(SUPPORTED_CHAT_MODELS)}"
            )
        return model

    @field_validator("username", "thread_id")
    @classmethod
    def validate_identifier(cls, value: str | None) -> str | None:
        if value is None:
            return None
        identifier = value.strip()
        return identifier or None


class SourceRef(BaseModel):
    source: str
    source_name: str
    doc_type: str
    page_number: int | None = None
    sheet_name: str | None = None


class StructuredAnswer(BaseModel):
    prompt: str
    bullets: list[str] = Field(default_factory=list)
    answer_text: str


class QueryMeta(BaseModel):
    chat_model: str = DEFAULT_CHAT_MODEL
    embedding_model: str = DEFAULT_EMBEDDING_MODEL
    k: int
    search_type: SearchType
    elapsed_ms: int
    thread_memory_used: bool = False
    thread_memory_ready: bool | None = None
    thread_id: str | None = None


class QueryResponse(BaseModel):
    answer: str
    structured: StructuredAnswer | None = None
    sources: list[SourceRef]
    meta: QueryMeta


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    collection: str
    db_path: str
    thread_memory_enabled: bool = False
    thread_memory_ready: bool = False
    threads_db: str | None = None
    thread_memory_error: str | None = None


class ThreadSummary(BaseModel):
    thread_id: str
    title: str
    created_at: datetime
    updated_at: datetime
    message_count: int = Field(default=0, ge=0)
    last_message_preview: str | None = None


class ListThreadsResponse(BaseModel):
    threads: list[ThreadSummary] = Field(default_factory=list)


class CreateThreadRequest(BaseModel):
    username: str = Field(..., min_length=1)
    thread_id: str | None = None
    title: str | None = None

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        username = value.strip()
        if not username:
            raise ValueError("username must not be blank")
        return username

    @field_validator("thread_id", "title")
    @classmethod
    def validate_optional(cls, value: str | None) -> str | None:
        if value is None:
            return None
        clean = value.strip()
        return clean or None


class CreateThreadResponse(BaseModel):
    thread: ThreadSummary


class RenameThreadRequest(BaseModel):
    username: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)

    @field_validator("username", "title")
    @classmethod
    def validate_non_blank(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("value must not be blank")
        return cleaned


class RenameThreadResponse(BaseModel):
    thread: ThreadSummary


class DeleteThreadResponse(BaseModel):
    deleted: bool = True
    thread_id: str


class ThreadMessageItem(BaseModel):
    id: int
    role: RoleType
    content: str
    created_at: datetime
    structured: StructuredAnswer | None = None
    sources: list[SourceRef] = Field(default_factory=list)


class GetThreadMessagesResponse(BaseModel):
    thread: ThreadSummary
    messages: list[ThreadMessageItem] = Field(default_factory=list)
