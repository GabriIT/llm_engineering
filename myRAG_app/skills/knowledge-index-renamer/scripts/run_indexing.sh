#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-$ROOT_DIR/.venv/bin/python}"
SCRIPT_PATH="$ROOT_DIR/myRAG_app/skills/knowledge-index-renamer/scripts/build_indexed_knowledge.py"

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "Python interpreter not found at: $PYTHON_BIN" >&2
  exit 2
fi

"$PYTHON_BIN" "$SCRIPT_PATH" "$@"
