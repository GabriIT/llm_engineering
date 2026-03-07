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
myrag_enforce_or_inject_knowledge_root "$PYTHON_BIN" "$@"

cd "$ROOT_DIR"
exec "$PYTHON_BIN" -m myRAG_app.parser.incremental_source_pipeline "${MYRAG_KNOWLEDGE_EXTRA_ARGS[@]}" "$@"
