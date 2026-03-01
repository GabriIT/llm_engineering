from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage, convert_to_messages
from langchain_openai import ChatOpenAI

from .config import (
    DEFAULT_CHAT_MODEL,
    DEFAULT_COLLECTION_NAME,
    DEFAULT_DB_PATH,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_RETRIEVAL_FETCH_K,
    DEFAULT_RETRIEVAL_K,
    DEFAULT_RETRIEVAL_LAMBDA_MULT,
    DEFAULT_RETRIEVAL_SEARCH_TYPE,
)
from .retrieval import retrieve_context

SYSTEM_PROMPT = """
You are a knowledgeable assistant for myRAG knowledge.
Use only the retrieved context as evidence.
If context is partially relevant, provide the best possible answer and clearly label uncertainty.
If context is truly insufficient, say: "I do not know based on the provided documents."
Include short source citations using [source_name] or [source_name p.X] when possible.
Context:
{context}
""".strip()


def _combined_query(question: str, history: list[dict] | None) -> str:
    if not history:
        return question
    prior_questions = [m.get("content", "") for m in history if m.get("role") == "user"]
    return "\n".join([*prior_questions, question]).strip()


def _format_context(docs: list[Document]) -> str:
    if not docs:
        return "(no retrieved context)"

    parts: list[str] = []
    for idx, doc in enumerate(docs, start=1):
        source_name = doc.metadata.get("source_name", "unknown")
        doc_type = doc.metadata.get("doc_type", "unknown")
        page = doc.metadata.get("page_number")
        sheet = doc.metadata.get("sheet_name")

        locator = []
        if page:
            locator.append(f"page={page}")
        if sheet:
            locator.append(f"sheet={sheet}")
        locator_text = f" ({', '.join(locator)})" if locator else ""

        parts.append(
            f"[{idx}] source={source_name} doc_type={doc_type}{locator_text}\n{doc.page_content}"
        )
    return "\n\n---\n\n".join(parts)


def answer_question(
    question: str,
    history: list[dict] | None = None,
    *,
    db_path: Path = DEFAULT_DB_PATH,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    embedding_model: str = DEFAULT_EMBEDDING_MODEL,
    chat_model: str = DEFAULT_CHAT_MODEL,
    k: int = DEFAULT_RETRIEVAL_K,
    search_type: str = DEFAULT_RETRIEVAL_SEARCH_TYPE,
    fetch_k: int = DEFAULT_RETRIEVAL_FETCH_K,
    lambda_mult: float = DEFAULT_RETRIEVAL_LAMBDA_MULT,
    doc_type: str | None = None,
    source_contains: str | None = None,
) -> tuple[str, list[Document]]:
    load_dotenv(override=True)
    query = _combined_query(question, history)
    docs = retrieve_context(
        query,
        db_path=db_path,
        collection_name=collection_name,
        embedding_model=embedding_model,
        k=k,
        search_type=search_type,
        fetch_k=fetch_k,
        lambda_mult=lambda_mult,
        doc_type=doc_type,
        source_contains=source_contains,
    )
    context = _format_context(docs)
    llm = ChatOpenAI(model_name=chat_model, temperature=0)

    messages = [SystemMessage(content=SYSTEM_PROMPT.format(context=context))]
    if history:
        messages.extend(convert_to_messages(history))
    messages.append(HumanMessage(content=question))
    response = llm.invoke(messages)
    return response.content, docs
