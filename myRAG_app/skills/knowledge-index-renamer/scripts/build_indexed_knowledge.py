#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
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


@dataclass(slots=True)
class IndexStateRecord:
    source_path: str
    target_path: str
    subfolder: str
    index: int
    date: str
    fingerprint: str


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
        "--mode",
        choices=["full", "incremental"],
        default="full",
        help="Index build mode (default: full).",
    )
    parser.add_argument(
        "--state-path",
        help="Optional JSON state file for incremental mode (default: <output_root>/.knowledge_index_state.json).",
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
    parser.add_argument(
        "--keep-deleted",
        action="store_true",
        help="In incremental mode, keep indexed files whose source was deleted.",
    )
    parser.add_argument(
        "--tracking-csv-path",
        help="Optional CSV output path for source->indexed tracking list.",
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


def _fingerprint(path: Path) -> str:
    stat = path.stat()
    return f"{stat.st_size}:{stat.st_mtime_ns}"


def _resolve_state_path(output_root: Path, raw_state_path: str | None) -> Path:
    if raw_state_path:
        return Path(raw_state_path).expanduser().resolve()
    return output_root / ".knowledge_index_state.json"


def _load_state(state_path: Path) -> dict[str, IndexStateRecord]:
    if not state_path.exists():
        return {}
    try:
        payload = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    records = payload.get("records", [])
    if not isinstance(records, list):
        return {}
    state: dict[str, IndexStateRecord] = {}
    for item in records:
        if not isinstance(item, dict):
            continue
        source_path = str(item.get("source_path", ""))
        target_path = str(item.get("target_path", ""))
        subfolder = str(item.get("subfolder", ""))
        if not source_path or not target_path or not subfolder:
            continue
        try:
            index = int(item.get("index", 0))
        except Exception:
            index = 0
        if index <= 0:
            continue
        state[source_path] = IndexStateRecord(
            source_path=source_path,
            target_path=target_path,
            subfolder=subfolder,
            index=index,
            date=str(item.get("date", "")),
            fingerprint=str(item.get("fingerprint", "")),
        )
    return state


def _save_state(state_path: Path, records: list[IndexStateRecord]) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "records": [asdict(record) for record in records],
    }
    state_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


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


def _build_full_state_records(
    mappings: list[MappingRecord], source_by_path: dict[str, Path], dry_run: bool
) -> list[IndexStateRecord]:
    records: list[IndexStateRecord] = []
    for mapping in mappings:
        source = source_by_path.get(mapping.source_path)
        if not source:
            continue
        fingerprint = ""
        if not dry_run:
            fingerprint = _fingerprint(source)
        records.append(
            IndexStateRecord(
                source_path=mapping.source_path,
                target_path=mapping.target_path,
                subfolder=mapping.subfolder,
                index=mapping.index,
                date=mapping.date,
                fingerprint=fingerprint,
            )
        )
    return records


def _build_incremental_mappings(
    *,
    files: list[Path],
    input_root: Path,
    output_root: Path,
    date_token: str,
    dry_run: bool,
    old_state: dict[str, IndexStateRecord],
    keep_deleted: bool,
) -> tuple[list[MappingRecord], list[IndexStateRecord], dict[str, int]]:
    current_by_source: dict[str, Path] = {str(path): path for path in files}
    removed_sources = sorted(set(old_state.keys()) - set(current_by_source.keys()))

    if not dry_run and not keep_deleted:
        for source_path in removed_sources:
            old = old_state[source_path]
            target_path = Path(old.target_path)
            if target_path.exists():
                target_path.unlink()

    used_indexes: dict[str, set[int]] = defaultdict(set)
    next_index: dict[str, int] = defaultdict(int)
    for record in old_state.values():
        if record.index <= 0:
            continue
        used_indexes[record.subfolder].add(record.index)
        if record.index > next_index[record.subfolder]:
            next_index[record.subfolder] = record.index

    ordered_files = sorted(
        files,
        key=lambda p: (str(p.relative_to(input_root).parent).casefold(), p.name.casefold()),
    )
    mappings: list[MappingRecord] = []
    new_state: list[IndexStateRecord] = []
    copied_count = 0
    unchanged_count = 0

    for source_path in ordered_files:
        rel = source_path.relative_to(input_root)
        subfolder = str(rel.parent)
        folder_name = rel.parent.name
        ext = "".join(source_path.suffixes)
        source_key = str(source_path)
        fp = _fingerprint(source_path) if not dry_run else ""
        old = old_state.get(source_key)

        keep_old_mapping = False
        if old and old.subfolder == subfolder and old.index > 0:
            old_target = Path(old.target_path).expanduser().resolve()
            expected_parent = (output_root / rel.parent).resolve()
            if old_target.parent == expected_parent:
                index = old.index
                target_path = old_target
                keep_old_mapping = True
                used_indexes[subfolder].add(index)
                if index > next_index[subfolder]:
                    next_index[subfolder] = index

        if not keep_old_mapping:
            index = next_index[subfolder] + 1
            while index in used_indexes[subfolder]:
                index += 1
            target_name = f"{folder_name}_{index}_{date_token}{ext}"
            target_path = (output_root / rel.parent / target_name).resolve()
            while not dry_run and target_path.exists():
                index += 1
                target_name = f"{folder_name}_{index}_{date_token}{ext}"
                target_path = (output_root / rel.parent / target_name).resolve()
            used_indexes[subfolder].add(index)
            next_index[subfolder] = index
            if not dry_run:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_path, target_path)
            copied_count += 1
            date_value = date_token
        else:
            if not dry_run:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                if old.fingerprint != fp or not target_path.exists():
                    shutil.copy2(source_path, target_path)
                    copied_count += 1
                else:
                    unchanged_count += 1
            date_value = old.date or date_token

        mappings.append(
            MappingRecord(
                source_path=source_key,
                target_path=str(target_path),
                subfolder=subfolder,
                index=index,
                date=date_value,
            )
        )
        new_state.append(
            IndexStateRecord(
                source_path=source_key,
                target_path=str(target_path),
                subfolder=subfolder,
                index=index,
                date=date_value,
                fingerprint=fp,
            )
        )

    if not dry_run and not keep_deleted and output_root.exists():
        for maybe_dir in sorted(output_root.rglob("*"), reverse=True):
            if maybe_dir.is_dir():
                try:
                    maybe_dir.rmdir()
                except OSError:
                    pass

    stats = {
        "copied_count": copied_count,
        "unchanged_count": unchanged_count,
        "removed_count": len(removed_sources) if not keep_deleted else 0,
    }
    return mappings, new_state, stats


def _write_tracking_csv(path: Path, mappings: list[MappingRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(mappings, key=lambda x: (x.subfolder.casefold(), x.index, x.source_path.casefold()))
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "source_path",
                "source_name",
                "indexed_path",
                "indexed_name",
                "subfolder",
                "index",
                "date",
            ]
        )
        for item in ordered:
            writer.writerow(
                [
                    item.source_path,
                    Path(item.source_path).name,
                    item.target_path,
                    Path(item.target_path).name,
                    item.subfolder,
                    item.index,
                    item.date,
                ]
            )


def _write_report(
    report_path: Path,
    mappings: list[MappingRecord],
    *,
    dry_run: bool,
    mode: str,
    state_path: Path,
    copied_count: int,
    unchanged_count: int,
    removed_count: int,
    tracking_csv_path: Path | None,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    by_subfolder: dict[str, int] = defaultdict(int)
    for item in mappings:
        by_subfolder[item.subfolder] += 1
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
        "mode": mode,
        "total_files": len(mappings),
        "copied_count": copied_count,
        "unchanged_count": unchanged_count,
        "removed_count": removed_count,
        "state_path": str(state_path),
        "tracking_csv_path": str(tracking_csv_path) if tracking_csv_path else None,
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
    mode = args.mode
    state_path = _resolve_state_path(output_root, args.state_path)
    tracking_csv_path = (
        Path(args.tracking_csv_path).expanduser().resolve() if args.tracking_csv_path else None
    )

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

    source_by_path = {str(path): path for path in source_files}

    if mode == "full":
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
        state_records = _build_full_state_records(mappings, source_by_path, args.dry_run)
        copied_count = 0 if args.dry_run else len(mappings)
        unchanged_count = 0
        removed_count = 0
    else:
        if args.clean_output and not args.dry_run:
            _clean_dir(output_root)
        if not args.dry_run:
            output_root.mkdir(parents=True, exist_ok=True)
        old_state = _load_state(state_path)
        mappings, state_records, stats = _build_incremental_mappings(
            files=source_files,
            input_root=input_root,
            output_root=output_root,
            date_token=date_token,
            dry_run=args.dry_run,
            old_state=old_state,
            keep_deleted=args.keep_deleted,
        )
        copied_count = stats["copied_count"]
        unchanged_count = stats["unchanged_count"]
        removed_count = stats["removed_count"]

    mappings = sorted(
        mappings, key=lambda x: (x.subfolder.casefold(), x.index, x.source_path.casefold())
    )
    state_records = sorted(
        state_records, key=lambda x: (x.subfolder.casefold(), x.index, x.source_path.casefold())
    )

    if not args.dry_run:
        _save_state(state_path, state_records)
    if tracking_csv_path:
        _write_tracking_csv(tracking_csv_path, mappings)

    _write_report(
        report_path,
        mappings,
        dry_run=args.dry_run,
        mode=mode,
        state_path=state_path,
        copied_count=copied_count,
        unchanged_count=unchanged_count,
        removed_count=removed_count,
        tracking_csv_path=tracking_csv_path,
    )

    print("=== Knowledge Index Build Summary ===")
    print(f"Input root: {input_root}")
    print(f"Output root: {output_root}")
    print(f"Date token: {date_token}")
    print(f"Mode: {mode}")
    print(f"Dry run: {args.dry_run}")
    print(f"Files mapped: {len(mappings)}")
    print(f"Files copied: {copied_count}")
    print(f"Files unchanged: {unchanged_count}")
    print(f"Files removed: {removed_count}")
    print(f"State: {state_path}")
    print(f"Report: {report_path}")
    if tracking_csv_path:
        print(f"Tracking CSV: {tracking_csv_path}")
    if mappings:
        print("Sample mappings:")
        for sample in mappings[:5]:
            print(f"- {sample.source_path} -> {sample.target_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
