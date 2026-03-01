from __future__ import annotations

import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient
from langchain_core.documents import Document

from myRAG_app.api.server import create_app


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

    @patch("myRAG_app.api.server.answer_question")
    def test_query_success(self, mock_answer_question) -> None:
        mock_answer_question.return_value = (
            "Answer text",
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
        self.assertEqual(payload["answer"], "Answer text")
        self.assertEqual(payload["meta"]["k"], 9)
        self.assertEqual(payload["meta"]["search_type"], "mmr")
        self.assertEqual(len(payload["sources"]), 1)
        self.assertEqual(payload["sources"][0]["source_name"], "source.pdf")

    def test_query_validation(self) -> None:
        response = self.client.post("/api/rag/query", json={"question": "   "})
        self.assertIn(response.status_code, {400, 422})

    @patch("myRAG_app.api.server.answer_question")
    def test_query_backend_error(self, mock_answer_question) -> None:
        mock_answer_question.side_effect = RuntimeError("backend exploded")
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
