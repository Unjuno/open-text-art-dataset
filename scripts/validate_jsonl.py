#!/usr/bin/env python3
"""Validate JSONL dataset files against a JSON Schema.

Usage:
    python scripts/validate_jsonl.py data/samples.jsonl
    python scripts/validate_jsonl.py data/samples.jsonl --schema schemas/entry.schema.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    print(
        "Missing dependency: jsonschema. Install with `python -m pip install jsonschema`.",
        file=sys.stderr,
    )
    sys.exit(2)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def iter_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                yield line_number, json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate dataset JSONL files.")
    parser.add_argument("jsonl", nargs="+", type=Path, help="JSONL file(s) to validate")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("schemas/entry.schema.json"),
        help="JSON Schema path",
    )
    args = parser.parse_args()

    schema = load_json(args.schema)
    validator = Draft202012Validator(schema)

    total = 0
    failed = 0
    seen_ids: set[str] = set()

    for jsonl_path in args.jsonl:
        if not jsonl_path.exists():
            print(f"Missing file: {jsonl_path}", file=sys.stderr)
            failed += 1
            continue

        for line_number, record in iter_jsonl(jsonl_path):
            total += 1
            errors = sorted(validator.iter_errors(record), key=lambda e: e.path)
            record_id = record.get("id") if isinstance(record, dict) else None

            if record_id in seen_ids:
                errors.append(ValueError(f"duplicate id: {record_id}"))
            elif isinstance(record_id, str):
                seen_ids.add(record_id)

            if errors:
                failed += 1
                print(f"FAIL {jsonl_path}:{line_number}", file=sys.stderr)
                for error in errors:
                    path = getattr(error, "json_path", "$")
                    message = getattr(error, "message", str(error))
                    print(f"  {path}: {message}", file=sys.stderr)

    if failed:
        print(f"Validation failed: {failed} invalid record(s), {total} checked.", file=sys.stderr)
        return 1

    print(f"Validation passed: {total} record(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
