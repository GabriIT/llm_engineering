# PPTX Hybrid RAG Demo

Note:
This folder is a demo/sandbox pipeline. Production PPTX ingestion is now integrated in
`myRAG_app` via the `pptx-rag-parser` skill and parser CLI modules.
Use:
`myRAG_app/parser/pptx_probe.py`
`myRAG_app/parser/audit.py`
`myRAG_app/vector/ingest_cli.py`

Files:
- `pptx_hybrid_rag_demo.py` — build/query script
- `requirements_pptx_rag.txt` — Python dependencies

System packages needed on Ubuntu:
```bash
sudo apt update
sudo apt install -y libreoffice poppler-utils
```

Python setup:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements_pptx_rag.txt
```

Pull models:
```bash
ollama pull qwen3.5:9b
ollama pull nomic-embed-text
```

Build chunks:
```bash
python3 pptx_hybrid_rag_demo.py build \
  --pptx "/mnt/data/202401 - Metal Replacement.pptx" \
  --outdir ./metal_replacement_rag \
  --vision-model qwen3.5:9b \
  --embed-model nomic-embed-text
```

Query:
```bash
python3 pptx_hybrid_rag_demo.py query \
  --chunk-dir ./metal_replacement_rag/chunks \
  --question "Which printer has finer stated precision and what are the two technologies compared?" \
  --vision-model qwen3.5:9b \
  --embed-model nomic-embed-text
```
