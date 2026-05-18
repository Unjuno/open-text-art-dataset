#!/usr/bin/env python3
"""Create a new data/entries/*.json file from the template.

Examples:
    python scripts/new_entry.py
    python scripts/new_entry.py --id text-art-000123
    python scripts/new_entry.py --art "orz" --meaning "despair" --context "完全に負けたorz"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "data" / "entries"
TEMPLATE_PATH = ROOT / "templates" / "entry.template.json"
ID_PATTERN = re.compile(r"^text-art-(\d{6})$")


def load_template() -> dict:
    return json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))


def existing_numbers() -> list[int]:
    numbers: list[int] = []
    for path in ENTRIES_DIR.glob("text-art-*.json"):
        match = ID_PATTERN.match(path.stem)
        if match:
            numbers.append(int(match.group(1)))
    return sorted(numbers)


def next_id() -> str:
    numbers = existing_numbers()
    next_number = numbers[-1] + 1 if numbers else 1
    return f"text-art-{next_number:06d}"


def count_lines(text: str) -> int:
    return text.count("\n") + 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new text-art dataset entry.")
    parser.add_argument("--id", dest="entry_id", help="Explicit entry ID, e.g. text-art-000011")
    parser.add_argument("--art", help="Text art string")
    parser.add_argument("--context", help="Example context text")
    parser.add_argument("--meaning", help="Intended meaning")
    parser.add_argument("--plain", help="Plain-text paraphrase")
    parser.add_argument("--art-type", default=None, help="art_type override")
    parser.add_argument("--charset", default=None, help="charset_class override")
    parser.add_argument("--review-status", default="draft", help="review_status value")
    args = parser.parse_args()

    entry_id = args.entry_id or next_id()
    if not ID_PATTERN.match(entry_id):
        print(f"Invalid id: {entry_id}. Expected text-art-000001 style.", file=sys.stderr)
        return 2

    output_path = ENTRIES_DIR / f"{entry_id}.json"
    if output_path.exists():
        print(f"Refusing to overwrite existing file: {output_path}", file=sys.stderr)
        return 1

    entry = load_template()
    entry["id"] = entry_id
    entry["review_status"] = args.review_status

    if args.art is not None:
        entry["art"] = args.art
        entry["line_count"] = count_lines(args.art)
    if args.context is not None:
        entry["context_text"] = args.context
    if args.meaning is not None:
        entry["intended_meaning"] = args.meaning
    if args.plain is not None:
        entry["plain_text"] = args.plain
    if args.art_type is not None:
        entry["art_type"] = args.art_type
    if args.charset is not None:
        entry["charset_class"] = args.charset

    ENTRIES_DIR.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(entry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
