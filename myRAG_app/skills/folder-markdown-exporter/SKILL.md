---
name: folder-markdown-exporter
description: Export parsed myRAG knowledge files into one markdown file per top-level knowledge subfolder, grouped by source with parse metadata and failed-file placeholders. Use when preparing human-readable corpus snapshots or markdown-based downstream ingestion.
---

# Folder Markdown Exporter

## Overview
Use this skill to convert parsed `.pdf`, `.docx`, and `.xlsx` knowledge content into folder-level markdown files.

## When To Use
1. You need one markdown file per top-level folder in `myRAG_knowledge`.
2. You want source-grouped markdown with parser provenance metadata.
3. You need explicit failed-file visibility instead of silent skips.

## Core Workflow
1. Run folder-level markdown export.
2. Review the JSON export report for failure counts and failed file details.
3. Spot-check generated markdown files for ordering and content quality.

## Commands
Run from repository root (`/home/gabri/udemy/llm_engineering`).

```bash
bash myRAG_app/skills/folder-markdown-exporter/scripts/export_folder_markdown.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --report-path /tmp/myrag_markdown_export_report.json
```

Strict mode:

```bash
bash myRAG_app/skills/folder-markdown-exporter/scripts/export_folder_markdown.sh \
  --knowledge-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --report-path /tmp/myrag_markdown_export_report.json \
  --strict
```

## Output Contract
1. One markdown file per top-level subfolder in knowledge root.
2. Markdown is grouped by source with segment ordering by page/sheet.
3. `Parse Failures` section is always present and includes actionable issue details.
4. JSON report includes summary counts, per-folder metrics, and failed-file records.

## References
1. `references/workflow.md`
2. `references/troubleshooting.md`
