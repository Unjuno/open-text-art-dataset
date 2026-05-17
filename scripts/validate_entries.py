#!/usr/bin/env python3
"""Validate data/entries/*.json files.

Checks:
- JSON syntax
- JSON Schema
- duplicate IDs
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


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    seen_ids: set[str] = set()
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
        if record_id in seen_ids:
            errors.append(ValueError(f"duplicate id: {record_id}"))
        elif isinstance(record_id, str):
            seen_ids.add(record_id)

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
