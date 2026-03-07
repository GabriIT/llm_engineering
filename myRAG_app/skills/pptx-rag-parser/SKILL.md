---
name: pptx-rag-parser
description: Parse and validate `.pptx` knowledge files for myRAG_app using text-first extraction with optional selective vision enrichment, then run audit/chunk/vectorstore flows with actionable failure reporting. Use when PPT/PPTX files must be ingested into RAG without breaking existing parser pipelines.
---

# PPTX RAG Parser

## Overview
Use this skill to ingest PowerPoint decks into the same parser/audit/vector pipeline used by myRAG documents.

## When To Use
1. You added `.pptx` files to `myRAG_knowledge` and need reliable parsing for RAG.
2. You need a single-file PPTX probe report before full ingestion.
3. You need strict parser gating for release/deployment.
4. You need selective vision enrichment for low-text slides only.

## Default Strategy
1. Text-first extraction from slide text, tables, and speaker notes.
2. Vision enrichment is optional and selective; disabled by default for cost/speed.
3. Keep full compatibility with existing `.pdf/.docx/.xlsx` flow.

## Core Workflow
1. Run incremental source->markdown->chunks pipeline:
`scripts/run_incremental_source_markdown_chunks.sh`
2. Probe a single PPTX:
`scripts/run_pptx_probe.sh`
3. Run full parser audit:
`scripts/run_pptx_audit.sh`
4. Build vectorstore:
`scripts/build_vectorstore_with_pptx.sh`
5. Inspect and query with existing parser/vector skills.

## Commands
Run from repository root (`/home/gabri/udemy/llm_engineering`).

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_incremental_source_markdown_chunks.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --markdown-output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge_incremental \
  --chunks-output-path /tmp/myrag_chunks_incremental.jsonl \
  --state-path /home/gabri/udemy/llm_engineering/myRAG_app/.state/incremental_source_manifest.json \
  --report-path /tmp/myrag_incremental_pipeline_report.json \
  --strict
```

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_probe.sh \
  --pptx-path "/home/gabri/udemy/llm_engineering/myRAG_knowledge/Metal_Replacement/202401 - Metal Replacement.pptx" \
  --report-path /tmp/myrag_pptx_probe.json
```

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/run_pptx_audit.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --report-path /tmp/myrag_parse_report.json \
  --strict
```

```bash
bash myRAG_app/skills/pptx-rag-parser/scripts/build_vectorstore_with_pptx.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --db-path /home/gabri/udemy/llm_engineering/myRAG_app/vector_db \
  --collection myrag_docs \
  --reset \
  --strict-parse
```

## Failure Handling
1. `pptx_primary_parser_unavailable`:
Install `python-pptx`.
2. `pptx_xml_fallback_failed`:
Deck may be corrupted or malformed; re-export PPTX.
3. `pptx_low_text`:
Enable selective vision mode for low-text slides.
4. `pptx_vision_failed`:
Verify `libreoffice`, `poppler-utils`, and Ollama endpoint/model.

## References
1. `references/workflow.md`
2. `references/troubleshooting.md`
