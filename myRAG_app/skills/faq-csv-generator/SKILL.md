---
name: faq-csv-generator
description: Generate FAQ CSV files from folder-level markdown inputs, producing at least 500 rows with columns Index, Question, Answer, and source. Use when preparing Q/A training data or searchable FAQ datasets from parsed myRAG markdown corpus.
---

# FAQ CSV Generator

## Overview
Use this skill to generate grounded rows from markdown files produced by the folder-markdown exporter.

## When To Use
1. You have markdown files containing `## Source:` sections and `### Segment` content.
2. You need a CSV FAQ or classification-style dataset with provenance (`markdown_filename::source_name`).
3. You need a row target gate (`>= 500` by default).

## Core Workflow
1. Run `scripts/generate_faq_csv.sh` with input markdown directory.
2. Verify output CSV has required columns and meets row threshold.
3. Review JSON report for warnings, per-source contribution, and shortfall causes.

## Commands
Run from repository root (`/home/gabri/udemy/llm_engineering`).

```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --output-csv /tmp/myrag_faq.csv \
  --report-path /tmp/myrag_faq_report.json \
  --min-rows 500
```

Strict mode:

```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --output-csv /tmp/myrag_faq.csv \
  --report-path /tmp/myrag_faq_report.json \
  --min-rows 500 \
  --strict
```

Classification-focused mode (recommended for training document-category behavior):

```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --output-csv /tmp/myrag_faq_classification.csv \
  --report-path /tmp/myrag_faq_classification_report.json \
  --min-rows 500 \
  --generation-mode classification
```

In `classification` mode, questions are normalized to:
`Which category should this document be classified under based on: <evidence>?`
and answers are normalized to start with:
`Category: <folder_name>.`

## Output Contract
1. CSV header is exactly: `Index,Question,Answer,source`.
2. `source` format is `<markdown_filename>::<source_name>`.
3. Row count is at least `--min-rows` unless non-strict mode allows shortfall.
4. JSON report records summary metrics, warnings, and per-source contributions.

## References
1. `references/workflow.md`
2. `references/troubleshooting.md`
