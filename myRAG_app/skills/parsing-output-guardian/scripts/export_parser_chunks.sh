#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-$ROOT_DIR/.venv/bin/python}"

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "Python interpreter not found at: $PYTHON_BIN" >&2
  exit 2
fi

# shellcheck source=/dev/null
source "$ROOT_DIR/myRAG_app/scripts/knowledge_root_bootstrap.sh"
myrag_load_repo_env "$ROOT_DIR"
myrag_set_knowledge_roots "$ROOT_DIR"
myrag_refresh_indexed_knowledge "$ROOT_DIR"
myrag_enforce_or_inject_knowledge_root "$PYTHON_BIN" "$@"

"$PYTHON_BIN" -m myRAG_app.parser.export_chunks "${MYRAG_KNOWLEDGE_EXTRA_ARGS[@]}" "$@"
