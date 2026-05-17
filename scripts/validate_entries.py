#!/usr/bin/env python3
"""Validate data/entries/*.json files.

Checks:
- JSON syntax
- JSON Schema
- duplicate IDs
- duplicate art strings
- line_count consistency
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "data" / "entries"
SCHEMA_PATH = ROOT / "schemas" / "entry.schema.json"


def count_lines(text: str) -> int:
    return text.count("\n") + 1


def normalize_art_for_duplicate_check(text: str) -> str:
    """Normalize only accidental outer whitespace.

    Do not Unicode-normalize or collapse inner spaces because text art can depend on
    exact characters and spacing.
    """

    return text.strip("\n")


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    seen_ids: dict[str, Path] = {}
    seen_art: dict[str, Path] = {}
    failed = 0
    checked = 0

    for path in sorted(ENTRIES_DIR.glob("*.json")):
        checked += 1

        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"FAIL {path}: invalid JSON: {exc}", file=sys.stderr)
            failed += 1
            continue

        errors = sorted(validator.iter_errors(record), key=lambda e: e.path)

        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in seen_ids:
                errors.append(
                    ValueError(f"duplicate id: {record_id} already used in {seen_ids[record_id]}")
                )
            else:
                seen_ids[record_id] = path

        art = record.get("art")
        if isinstance(art, str):
            art_key = normalize_art_for_duplicate_check(art)
            if art_key in seen_art:
                errors.append(
                    ValueError(
                        f"duplicate art string: same art already used in {seen_art[art_key]}"
                    )
                )
            else:
                seen_art[art_key] = path

        actual_lines = count_lines(record.get("art", ""))
        declared_lines = record.get("line_count")
        if declared_lines != actual_lines:
            errors.append(
                ValueError(
                    f"line_count mismatch: declared={declared_lines}, actual={actual_lines}"
                )
            )

        if errors:
            failed += 1
            print(f"FAIL {path}", file=sys.stderr)
            for error in errors:
                message = getattr(error, "message", str(error))
                print(f"  {message}", file=sys.stderr)

    if failed:
        print(f"Validation failed: {failed} invalid file(s), {checked} checked.", file=sys.stderr)
        return 1

    print(f"Validation passed: {checked} entry file(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
