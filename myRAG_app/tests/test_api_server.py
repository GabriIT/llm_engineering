from __future__ import annotations

import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient
from langchain_core.documents import Document

from myRAG_app.api.server import create_app
from myRAG_app.vector.answer import StructuredRagAnswer


class ApiServerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = TestClient(self.app)

    def test_health_ok(self) -> None:
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["status"], "ok")
        self.assertIn("collection", payload)
        self.assertIn("db_path", payload)

    @patch.dict("os.environ", {"MYRAG_ALLOWED_ORIGINS": "http://154.12.245.254,http://example.com"})
    def test_allowed_origins_from_env(self) -> None:
        app = create_app()
        cors_middlewares = [m for m in app.user_middleware if m.cls.__name__ == "CORSMiddleware"]
        self.assertEqual(len(cors_middlewares), 1)
        allow_origins = cors_middlewares[0].kwargs.get("allow_origins", [])
        self.assertEqual(allow_origins, ["http://154.12.245.254", "http://example.com"])

    @patch("myRAG_app.api.server.answer_question_structured")
    def test_query_success(self, mock_answer_question_structured) -> None:
        mock_answer_question_structured.return_value = (
            StructuredRagAnswer(
                prompt="What is in the certificate?",
                bullets=["Certificate states migration compliance.", "Validity date is listed."],
                answer_text="The certificate confirms migration compliance and states validity details.",
            ),
            "- Certificate states migration compliance.\n- Validity date is listed.\n\nThe certificate confirms migration compliance and states validity details.",
            [
                Document(
                    page_content="context",
                    metadata={
                        "source": "/tmp/source.pdf",
                        "source_name": "source.pdf",
                        "doc_type": "Certifications",
                        "page_number": 1,
                    },
                )
            ],
        )

        response = self.client.post(
            "/api/rag/query",
            json={
                "question": "What is in the certificate?",
                "history": [{"role": "user", "content": "Earlier question"}],
                "retrieval": {
                    "k": 9,
                    "search_type": "mmr",
                    "fetch_k": 40,
                    "lambda_mult": 0.35,
                },
            },
        )
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn("Certificate states migration compliance.", payload["answer"])
        self.assertEqual(payload["structured"]["prompt"], "What is in the certificate?")
        self.assertEqual(len(payload["structured"]["bullets"]), 2)
        self.assertEqual(payload["meta"]["k"], 9)
        self.assertEqual(payload["meta"]["search_type"], "mmr")
        self.assertEqual(payload["meta"]["chat_model"], "gpt-4.1-nano")
        self.assertEqual(len(payload["sources"]), 1)
        self.assertEqual(payload["sources"][0]["source_name"], "source.pdf")

    @patch("myRAG_app.api.server.answer_question_structured")
    def test_query_with_selected_chat_model(self, mock_answer_question_structured) -> None:
        mock_answer_question_structured.return_value = (
            StructuredRagAnswer(
                prompt="Classify this content",
                bullets=["Belongs to classification workflow."],
                answer_text="Category hint is available.",
            ),
            "- Belongs to classification workflow.\n\nCategory hint is available.",
            [],
        )
        response = self.client.post(
            "/api/rag/query",
            json={
                "question": "Classify this content",
                "chat_model": "qwen3.5:9b",
            },
        )
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["meta"]["chat_model"], "qwen3.5:9b")
        _, kwargs = mock_answer_question_structured.call_args
        self.assertEqual(kwargs["chat_model"], "qwen3.5:9b")

    def test_query_validation(self) -> None:
        response = self.client.post("/api/rag/query", json={"question": "   "})
        self.assertIn(response.status_code, {400, 422})

    def test_query_validation_invalid_chat_model(self) -> None:
        response = self.client.post(
            "/api/rag/query",
            json={"question": "Hello", "chat_model": "invalid-model"},
        )
        self.assertIn(response.status_code, {400, 422})

    @patch("myRAG_app.api.server.answer_question_structured")
    def test_query_backend_error(self, mock_answer_question_structured) -> None:
        mock_answer_question_structured.side_effect = RuntimeError("backend exploded")
        response = self.client.post(
            "/api/rag/query",
            json={"question": "Hello"},
        )
        self.assertEqual(response.status_code, 500)
        payload = response.json()
        self.assertEqual(payload["detail"]["error"], "backend_error")
        self.assertIn("backend exploded", payload["detail"]["message"])


if __name__ == "__main__":
    unittest.main()
