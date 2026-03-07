---
name: knowledge-index-renamer
description: Copy files from myRAG_knowledge into a new output tree and rename each file as subfoldername_index_YYYYMMDD.ext, with index starting at 1 for each subfolder. Use when preparing indexed and normalized knowledge snapshots before ingestion, archiving, or sharing with other apps.
---

# Knowledge Index Renamer

## Overview
Use this skill to build `myRAG_knowledge_index` from `myRAG_knowledge` while preserving folder structure and applying deterministic filename indexing.

## Core Workflow
1. Run dry-run first to preview source->target mappings and detect collisions.
2. Run indexing with `--clean-output` to regenerate `myRAG_knowledge_index`.
3. Review JSON report for counts and mapping records.
4. Export the skill folder as tarball when reusing in other apps.

## Commands
Run from repository root (`/home/gabri/udemy/llm_engineering`).

Dry run:
```bash
bash myRAG_app/skills/knowledge-index-renamer/scripts/run_indexing.sh \
  --input-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --report-path /tmp/myrag_knowledge_index_report.json \
  --dry-run
```

Create/update indexed output:
```bash
bash myRAG_app/skills/knowledge-index-renamer/scripts/run_indexing.sh \
  --input-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --report-path /tmp/myrag_knowledge_index_report.json \
  --clean-output
```

## Output Contract
1. Output root is `myRAG_knowledge_index`.
2. Subfolder tree is preserved.
3. Each file is renamed to:
`<subfolder_name>_<index>_<YYYYMMDD><original_ext>`
4. Index starts at `1` for each containing subfolder.
5. JSON report contains summary and per-file mapping.

## Export/Import Skill
Use `references/workflow.md` for exact commands to export this skill and import it into another app.

## References
1. `references/workflow.md`
2. `references/troubleshooting.md`
