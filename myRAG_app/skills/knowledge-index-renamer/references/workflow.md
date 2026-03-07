# Knowledge Index Renamer Workflow

## 1. Dry-run mapping preview
```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/skills/knowledge-index-renamer/scripts/run_indexing.sh \
  --input-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --report-path /tmp/myrag_knowledge_index_report.json \
  --dry-run
```

## 2. Build indexed output
```bash
cd /home/gabri/udemy/llm_engineering
bash myRAG_app/skills/knowledge-index-renamer/scripts/run_indexing.sh \
  --input-root /home/gabri/udemy/llm_engineering/myRAG_knowledge \
  --output-root /home/gabri/udemy/llm_engineering/myRAG_knowledge_index \
  --report-path /tmp/myrag_knowledge_index_report.json \
  --clean-output
```

## 3. Filename format and indexing rules
1. Name format:
`<subfolder_name>_<index>_<YYYYMMDD><ext>`
2. Index starts at `1` for each containing subfolder.
3. Subfolder tree remains unchanged under output root.

## 4. Export this skill for other apps
Create archive:
```bash
cd /home/gabri/udemy/llm_engineering/myRAG_app/skills
tar -czf /tmp/knowledge-index-renamer.tgz knowledge-index-renamer
```

## 5. Import in another app
```bash
mkdir -p /path/to/new_app/skills
tar -xzf /tmp/knowledge-index-renamer.tgz -C /path/to/new_app/skills
```

Validate imported skill:
```bash
python3 /home/gabri/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /path/to/new_app/skills/knowledge-index-renamer
```

Run in new app:
```bash
cd /path/to/new_app
bash skills/knowledge-index-renamer/scripts/run_indexing.sh \
  --input-root /path/to/new_app/myRAG_knowledge \
  --output-root /path/to/new_app/myRAG_knowledge_index \
  --report-path /tmp/new_app_knowledge_index_report.json \
  --clean-output
```
