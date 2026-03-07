# Knowledge Index Renamer - Usage Guide

This guide explains how to use the `knowledge-index-renamer` skill and scripts to copy files from `myRAG_knowledge` into `myRAG_knowledge_index` with deterministic indexed names.

## Purpose
Use this workflow when you want an indexed snapshot of your knowledge base with consistent filenames for ingestion, archiving, or sharing.

## Naming Rule
Each output file name is:
`<subfolder_name>_<index>_<YYYYMMDD><original_ext>`

Example:
`competitors_2_20260307.xlsx`

Rules:
1. Index starts at `1` for each containing subfolder.
2. Top-level and nested folder structure is preserved in output.
3. Original extension is preserved.

## Paths Used in This Project
1. Source root:
`/home/gabri/udemy/llm_engineering/myRAG_knowledge`
2. Output root:
`/home/gabri/udemy/llm_engineering/myRAG_knowledge_index`
3. Skill folder:
`/home/gabri/udemy/llm_engineering/myRAG_app/skills/knowledge-index-renamer`
4. Default report:
`/tmp/myrag_knowledge_index_report.json`

## Script Entry Points
1. Wrapper:
`myRAG_app/skills/knowledge-index-renamer/scripts/run_indexing.sh`
2. Python implementation:
`myRAG_app/skills/knowledge-index-renamer/scripts/build_indexed_knowledge.py`

## Quick Start
Run from repository root:
`/home/gabri/udemy/llm_engineering`

### 1) Dry-run (recommended first)
```bash
bash myRAG_app/skills/knowledge-index-renamer/scripts/run_indexing.sh \
  --input-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --report-path /tmp/myrag_knowledge_index_report.json \
  --dry-run
```

### 2) Build output (fresh rebuild)
```bash
bash myRAG_app/skills/knowledge-index-renamer/scripts/run_indexing.sh \
  --input-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --report-path /tmp/myrag_knowledge_index_report.json \
  --clean-output
```

## Common Options
1. Custom date token:
```bash
--date 20260307
```
2. Overwrite existing target files without cleaning first:
```bash
--overwrite
```
3. Show mapping only:
```bash
--dry-run
```

## Validation Commands
Compare source and output file counts:
```bash
find /home/gabri/udemy/llm_engineering/myRAG_knowledge -type f | wc -l
find /home/gabri/udemy/llm_engineering/myRAG_knowledge_index -type f | wc -l
```

Preview report:
```bash
sed -n '1,160p' /tmp/myrag_knowledge_index_report.json
```

## How to Activate as a Skill in Codex
Use the skill name in your prompt:
`$knowledge-index-renamer`

Example:
`Use $knowledge-index-renamer to rebuild myRAG_knowledge_index with today's date and generate a report.`

## Export This Skill for Other Apps
Create a portable archive:
```bash
cd /home/gabri/udemy/llm_engineering/myRAG_app/skills
tar -czf /tmp/knowledge-index-renamer.tgz knowledge-index-renamer
```

## Import and Use in a New App
1. Extract:
```bash
mkdir -p /path/to/new_app/skills
tar -xzf /tmp/knowledge-index-renamer.tgz -C /path/to/new_app/skills
```
2. Validate:
```bash
python3 /home/gabri/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /path/to/new_app/skills/knowledge-index-renamer
```
3. Run in the new app:
```bash
cd /path/to/new_app
bash skills/knowledge-index-renamer/scripts/run_indexing.sh \
  --input-root /path/to/new_app/myRAG_knowledge \
  --output-root /path/to/new_app/myRAG_knowledge_index \
  --report-path /tmp/new_app_knowledge_index_report.json \
  --clean-output
```

## Troubleshooting
1. Error: output root not empty
Use `--clean-output` or `--overwrite`.
2. Error: invalid date format
Use `--date` as 8 digits `YYYYMMDD`.
3. Error: no files found
Confirm files exist inside subfolders of input root.
4. Permission errors
Choose writable output/report paths.

