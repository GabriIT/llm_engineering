# FAQ CSV Workflow

## Purpose
Generate a FAQ CSV from folder-level markdown files with row target and source traceability.

## Standard Run
```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --output-csv /tmp/myrag_faq.csv \
  --report-path /tmp/myrag_faq_report.json \
  --min-rows 500
```

## Classification-Focused Run
```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --output-csv /tmp/myrag_faq_classification.csv \
  --report-path /tmp/myrag_faq_classification_report.json \
  --min-rows 500 \
  --generation-mode classification
```

## Alternate Input (previous generated test set)
```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /tmp/myrag_markdown_from_skill \
  --output-csv /tmp/myrag_faq_from_tmp.csv \
  --report-path /tmp/myrag_faq_report_from_tmp.json \
  --min-rows 500
```

## Strict Gate
```bash
bash myRAG_app/skills/faq-csv-generator/scripts/generate_faq_csv.sh \
  --input-dir /home/gabri/udemy/llm_engineering/myRAG_app/markdown_knowledge \
  --output-csv /tmp/myrag_faq.csv \
  --report-path /tmp/myrag_faq_report.json \
  --min-rows 500 \
  --strict
```

## Validation Checklist
1. CSV exists and header equals `Index,Question,Answer,source`.
2. Row count is `>= min_rows`.
3. `source` values include both markdown filename and original source name.
4. Report contains:
- `summary.rows_written`
- `summary.target_met`
- `per_markdown_file_counts`
- `per_source_counts`
- `warnings`
