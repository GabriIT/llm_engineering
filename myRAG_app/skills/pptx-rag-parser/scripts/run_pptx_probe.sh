#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-$ROOT_DIR/.venv/bin/python}"

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "Python interpreter not found: $PYTHON_BIN" >&2
  echo "Set PYTHON_BIN or create .venv first." >&2
  exit 2
fi

if [[ -f "$ROOT_DIR/.env" ]]; then
  set -a
  source "$ROOT_DIR/.env"
  set +a
fi

# shellcheck source=/dev/null
source "$ROOT_DIR/myRAG_app/scripts/knowledge_root_bootstrap.sh"
myrag_set_knowledge_roots "$ROOT_DIR"
myrag_refresh_indexed_knowledge "$ROOT_DIR"

pptx_path=""
ARGS=("$@")
for ((i = 0; i < ${#ARGS[@]}; i++)); do
  if [[ "${ARGS[$i]}" == "--pptx-path" ]]; then
    if ((i + 1 >= ${#ARGS[@]})); then
      echo "Missing value for --pptx-path" >&2
      exit 2
    fi
    pptx_path="${ARGS[$((i + 1))]}"
    break
  elif [[ "${ARGS[$i]}" == --pptx-path=* ]]; then
    pptx_path="${ARGS[$i]#--pptx-path=}"
    break
  fi
done

if [[ -n "$pptx_path" ]]; then
  resolved_pptx="$(
    "$PYTHON_BIN" -c 'from pathlib import Path; import sys; print(Path(sys.argv[1]).expanduser().resolve())' \
      "$pptx_path"
  )"
  resolved_index="$(
    "$PYTHON_BIN" -c 'from pathlib import Path; import sys; print(Path(sys.argv[1]).expanduser().resolve())' \
      "$MYRAG_KNOWLEDGE_ROOT"
  )"
  case "$resolved_pptx" in
    "$resolved_index"/*) ;;
    *)
      echo "This wrapper requires --pptx-path under indexed root: $resolved_index" >&2
      echo "Run with a file path from myRAG_knowledge_index." >&2
      exit 2
      ;;
  esac
fi

cd "$ROOT_DIR"
exec "$PYTHON_BIN" -m myRAG_app.parser.pptx_probe "$@"
