#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

MAX_RECOMMENDED_CHARS = 4000


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate parser-exported JSONL chunks for vector DB ingestion."
    )
    parser.add_argument("--input", required=True, help="Input JSONL file path.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero when warnings exist.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        return 2

    line_count = 0
    errors: list[str] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()

    with input_path.open("r", encoding="utf-8") as f:
        for idx, raw_line in enumerate(f, start=1):
            line_count += 1
            line = raw_line.strip()
            if not line:
                warnings.append(f"Line {idx}: empty line")
                continue

            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"Line {idx}: invalid JSON ({exc})")
                continue

            for key in ("id", "text", "metadata"):
                if key not in obj:
                    errors.append(f"Line {idx}: missing key '{key}'")

            chunk_id = obj.get("id")
            text = obj.get("text")
            metadata = obj.get("metadata")

            if not isinstance(chunk_id, str) or not chunk_id.strip():
                errors.append(f"Line {idx}: invalid id")
            elif chunk_id in seen_ids:
                errors.append(f"Line {idx}: duplicate id '{chunk_id}'")
            else:
                seen_ids.add(chunk_id)

            if not isinstance(text, str) or not text.strip():
                errors.append(f"Line {idx}: empty text")
            elif len(text) > MAX_RECOMMENDED_CHARS:
                warnings.append(
                    f"Line {idx}: large chunk text ({len(text)} chars) exceeds recommended "
                    f"{MAX_RECOMMENDED_CHARS}"
                )

            if not isinstance(metadata, dict):
                errors.append(f"Line {idx}: metadata must be an object")
            else:
                for mkey in ("source", "doc_type", "chunk_index"):
                    if mkey not in metadata:
                        warnings.append(f"Line {idx}: metadata missing '{mkey}'")

    print("=== Chunk JSONL Validation Summary ===")
    print(f"File: {input_path}")
    print(f"Lines processed: {line_count}")
    print(f"Unique IDs: {len(seen_ids)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("\nErrors:")
        for msg in errors[:50]:
            print(f"- {msg}")
        if len(errors) > 50:
            print(f"- ... and {len(errors) - 50} more")

    if warnings:
        print("\nWarnings:")
        for msg in warnings[:50]:
            print(f"- {msg}")
        if len(warnings) > 50:
            print(f"- ... and {len(warnings) - 50} more")

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

