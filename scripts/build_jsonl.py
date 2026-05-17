#!/usr/bin/env python3
"""Build JSONL artifacts from data/entries/*.json.

Usage:
    python scripts/build_jsonl.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "data" / "entries"
SAMPLES_PATH = ROOT / "data" / "samples.jsonl"
REVIEWED_PATH = ROOT / "data" / "reviewed" / "v0.1.jsonl"


def load_entries():
    entries = []
    for path in sorted(ENTRIES_DIR.glob("*.json")):
        entries.append(json.loads(path.read_text(encoding="utf-8")))
    return entries


def write_jsonl(path: Path, entries):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(json.dumps(entry, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")


def main() -> int:
    entries = load_entries()
    write_jsonl(SAMPLES_PATH, entries)
    reviewed_entries = [e for e in entries if e.get("review_status") == "reviewed"]
    write_jsonl(REVIEWED_PATH, reviewed_entries)

    print(f"Built {len(entries)} entries.")
    print(f"Wrote: {SAMPLES_PATH}")
    print(f"Wrote: {REVIEWED_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
