# myRAG Workflow Explanation

## Scope
This document summarizes, in chronological order, what was added from the first request through the current state of `myRAG_app`, the goal of each step, and the resulting artifacts.

## Step-by-Step Build History
1. Multi-format parser foundation.
Goal: parse mixed files in `myRAG_knowledge` (`.pdf`, `.docx`, `.xlsx`) into LangChain `Document` objects.
Added: parser module with file discovery, format dispatch, normalization, and metadata.

2. Audit-first parsing workflow.
Goal: avoid silent failures and produce actionable diagnostics.
Added: parse result dataclasses, status/issue classification, JSON report writer, CLI summary.

3. Format fallbacks and quality checks.
Goal: increase extraction reliability for hard files.
Added:
- PDF fallback chain (`PyPDFLoader` then `pdftotext`), low-text detection, scan/image-only warning.
- DOCX fallback (XML extraction when primary fails).
- XLSX fallback (XML cell extraction when primary fails).

4. OCR path for scan-like PDFs.
Goal: recover text from image-only PDFs.
Added: OCR fallback support (`pymupdf`, `rapidocr-onnxruntime`, `pillow`) and issue guidance in reports.

5. Parsing tests.
Goal: validate routing, thresholds, failures, and integration on the real corpus.
Added: unit + integration tests for parser behavior and CLI outcomes.

6. Chunk export and validation.
Goal: produce structured chunk output suitable for vector ingestion and quality control.
Added: chunk export module/CLI and validation scripts for JSONL integrity.

7. Parsing skill hardening.
Goal: standardize recurring parse/audit/build workflows.
Added: `parsing-output-guardian` skill with wrappers for audit, chunk export, validation, vector build, inspect, and query smoke test.

8. LangChain + Chroma RAG baseline.
Goal: enable local RAG retrieval and answering with the same model family.
Added: ingestion/query/inspect modules and CLI commands with Chroma persistence.

9. Vectorstore upgrade with backup and rollback.
Goal: safely rebuild vector DB after source updates.
Added: `upgrade_cli` (candidate build + promote + backup) and rollback script (`rollback_vector_db.sh`).

10. API + TypeScript UI.
Goal: provide interactive app usage beyond CLI.
Added:
- FastAPI backend (`/api/health`, `/api/rag/query`).
- React + Vite TypeScript UI with pseudo-auth, thread history, sidebar thread selection, and multi-turn chat.

11. Structured response presentation.
Goal: improve output readability for operations/training review.
Added:
- Answer structure: prompt, concise bullets, short answer text, sources.
- UI toggle: structured view vs raw answer view.

12. Model selection from UI.
Goal: runtime selection between default cloud model and local Ollama models.
Added: model dropdown and backend support for `gpt-4.1-nano`, `qwen3.5:9b`, `llama3.2:latest`.

13. Deployment runbooks and scripts.
Goal: non-disruptive VPS deployment under `/RAG-mat` with reverse proxy.
Added: Docker Compose deployment assets, precheck/build/copy scripts, and operational runbooks.

14. Folder-level markdown export.
Goal: generate one markdown file per top-level knowledge folder for transparent corpus snapshots.
Added: markdown exporter module/CLI and `folder-markdown-exporter` skill.

15. FAQ CSV generation from markdown.
Goal: derive large QA datasets (`Index, Question, Answer, source`) from markdown sources.
Added: FAQ generation module/CLI, quality filtering, deduplication, classification-oriented mode, and `faq-csv-generator` skill.

16. Knowledge indexing and renaming skill.
Goal: create normalized, shareable snapshots named as `subfolder_index_YYYYMMDD.ext`.
Added: `knowledge-index-renamer` skill with scripts to build `myRAG_knowledge_index`.

17. Markdown-based vectorstore flow.
Goal: build and manage a second vector DB sourced from markdown snapshots.
Added: `markdown_upgrade_cli` + dedicated runbook for candidate/promote/active-store selection.

18. Runtime configuration clarification.
Goal: make active vectorstore explicit and predictable.
Added documentation for `MYRAG_DB_PATH` and `MYRAG_COLLECTION`, with recommended API startup:
`uvicorn ... --env-file .env`.

## Skills Created
1. `parsing-output-guardian`
Description: run and safeguard parse -> audit -> chunk validation -> vector build/inspect/query for mixed knowledge formats.
Path: `/home/gabri/udemy/llm_engineering/myRAG_app/skills/parsing-output-guardian/SKILL.md`

2. `folder-markdown-exporter`
Description: export parsed knowledge into one markdown per top-level folder, grouped by source, including parse metadata and failure placeholders.
Path: `/home/gabri/udemy/llm_engineering/myRAG_app/skills/folder-markdown-exporter/SKILL.md`

3. `faq-csv-generator`
Description: generate FAQ CSV datasets from markdown inputs with required schema and high-row-count targets for downstream training/search.
Path: `/home/gabri/udemy/llm_engineering/myRAG_app/skills/faq-csv-generator/SKILL.md`

4. `knowledge-index-renamer`
Description: copy and rename knowledge files into indexed naming format per subfolder for normalized snapshots and sharing across apps.
Path: `/home/gabri/udemy/llm_engineering/myRAG_app/skills/knowledge-index-renamer/SKILL.md`

## Current Operational Outcome
1. You can parse heterogeneous files with explicit audit and fallback visibility.
2. You can build, inspect, upgrade, and roll back vectorstores safely.
3. You can run RAG via CLI, API, and UI with selectable chat models.
4. You can produce markdown snapshots and FAQ datasets for review/training workflows.
