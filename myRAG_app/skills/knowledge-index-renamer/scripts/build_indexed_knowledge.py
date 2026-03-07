#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(slots=True)
class MappingRecord:
    source_path: str
    target_path: str
    subfolder: str
    index: int
    date: str


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Copy files from source knowledge tree into an indexed tree where file names follow "
            "<subfolder>_<index>_<YYYYMMDD><ext>."
        )
    )
    parser.add_argument("--input-root", required=True, help="Source knowledge root.")
    parser.add_argument("--output-root", required=True, help="Output knowledge index root.")
    parser.add_argument(
        "--report-path",
        default="/tmp/myrag_knowledge_index_report.json",
        help="JSON report path (default: /tmp/myrag_knowledge_index_report.json).",
    )
    parser.add_argument(
        "--date",
        default=datetime.now().strftime("%Y%m%d"),
        help="Date token for output names (default: today in YYYYMMDD).",
    )
    parser.add_argument(
        "--clean-output",
        action="store_true",
        help="Remove output-root before writing.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print/report mapping without writing files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow overwriting existing target files when output root already exists.",
    )
    return parser


def _iter_source_files(input_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(input_root.rglob("*"), key=lambda p: str(p).casefold()):
        if not path.is_file():
            continue
        rel = path.relative_to(input_root)
        if len(rel.parts) < 2:
            # Skip files directly under input root; include only files inside sub-folders.
            continue
        files.append(path)
    return files


def _clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


def _validate_output_policy(
    output_root: Path, *, clean_output: bool, dry_run: bool, overwrite: bool
) -> None:
    if dry_run:
        return
    if clean_output:
        _clean_dir(output_root)
        return
    if output_root.exists() and any(output_root.iterdir()) and not overwrite:
        raise RuntimeError(
            f"Output root already contains files: {output_root}. "
            "Use --clean-output or --overwrite."
        )


def _copy_with_index(
    files: list[Path], input_root: Path, output_root: Path, date_token: str, dry_run: bool
) -> list[MappingRecord]:
    grouped: dict[Path, list[Path]] = defaultdict(list)
    for path in files:
        rel = path.relative_to(input_root)
        grouped[rel.parent].append(path)

    mappings: list[MappingRecord] = []
    for rel_parent in sorted(grouped.keys(), key=lambda p: str(p).casefold()):
        folder_name = rel_parent.name
        current_files = sorted(grouped[rel_parent], key=lambda p: p.name.casefold())
        for idx, source_path in enumerate(current_files, start=1):
            ext = "".join(source_path.suffixes)
            target_name = f"{folder_name}_{idx}_{date_token}{ext}"
            target_path = output_root / rel_parent / target_name
            mappings.append(
                MappingRecord(
                    source_path=str(source_path),
                    target_path=str(target_path),
                    subfolder=str(rel_parent),
                    index=idx,
                    date=date_token,
                )
            )
            if dry_run:
                continue
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, target_path)

    return mappings


def _write_report(report_path: Path, mappings: list[MappingRecord], dry_run: bool) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    by_subfolder: dict[str, int] = defaultdict(int)
    for item in mappings:
        by_subfolder[item.subfolder] += 1
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
        "total_files": len(mappings),
        "subfolder_counts": dict(sorted(by_subfolder.items())),
        "mappings": [asdict(record) for record in mappings],
    }
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    input_root = Path(args.input_root).expanduser().resolve()
    output_root = Path(args.output_root).expanduser().resolve()
    report_path = Path(args.report_path).expanduser().resolve()
    date_token = args.date.strip()

    if not input_root.exists() or not input_root.is_dir():
        print(f"Input root does not exist or is not a directory: {input_root}")
        return 2
    if len(date_token) != 8 or not date_token.isdigit():
        print("--date must be in YYYYMMDD format.")
        return 2

    source_files = _iter_source_files(input_root)
    if not source_files:
        print("No files found inside sub-folders of input root.")
        return 2

    try:
        _validate_output_policy(
            output_root,
            clean_output=args.clean_output,
            dry_run=args.dry_run,
            overwrite=args.overwrite,
        )
    except RuntimeError as exc:
        print(str(exc))
        return 2

    mappings = _copy_with_index(
        source_files,
        input_root=input_root,
        output_root=output_root,
        date_token=date_token,
        dry_run=args.dry_run,
    )
    _write_report(report_path, mappings, dry_run=args.dry_run)

    print("=== Knowledge Index Build Summary ===")
    print(f"Input root: {input_root}")
    print(f"Output root: {output_root}")
    print(f"Date token: {date_token}")
    print(f"Dry run: {args.dry_run}")
    print(f"Files mapped: {len(mappings)}")
    print(f"Report: {report_path}")
    if mappings:
        print("Sample mappings:")
        for sample in mappings[:5]:
            print(f"- {sample.source_path} -> {sample.target_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
