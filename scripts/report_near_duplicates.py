#!/usr/bin/env python3
"""Report near-duplicate text-art entries.

This script does not fail by default. It prints candidate pairs so reviewers can
inspect them manually. Exact duplicate `art` strings are already rejected by
scripts/validate_entries.py.
"""

from __future__ import annotations

import argparse
import json
import re
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "data" / "entries"


def load_entries() -> list[tuple[Path, dict]]:
    entries: list[tuple[Path, dict]] = []
    for path in sorted(ENTRIES_DIR.glob("*.json")):
        entries.append((path, json.loads(path.read_text(encoding="utf-8"))))
    return entries


def compact_for_similarity(text: str) -> str:
    """Reduce obvious accidental whitespace for fuzzy comparison.

    This is for reporting only. Do not use this to rewrite dataset content.
    """

    return re.sub(r"\s+", "", text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Report near-duplicate text-art entries.")
    parser.add_argument("--threshold", type=float, default=0.85, help="Similarity threshold")
    parser.add_argument("--fail-on-match", action="store_true", help="Exit 1 if candidates are found")
    args = parser.parse_args()

    entries = load_entries()
    candidates: list[tuple[float, Path, Path, str, str]] = []

    for i, (left_path, left) in enumerate(entries):
        left_art = str(left.get("art", ""))
        left_key = compact_for_similarity(left_art)
        for right_path, right in entries[i + 1 :]:
            right_art = str(right.get("art", ""))
            right_key = compact_for_similarity(right_art)
            if not left_key or not right_key:
                continue
            score = SequenceMatcher(None, left_key, right_key).ratio()
            if score >= args.threshold:
                candidates.append((score, left_path, right_path, left_art, right_art))

    if not candidates:
        print("No near-duplicate candidates found.")
        return 0

    print("Near-duplicate candidates:")
    for score, left_path, right_path, left_art, right_art in sorted(candidates, reverse=True):
        print(f"- score={score:.3f}: {left_path} <-> {right_path}")
        print(f"  left : {left_art!r}")
        print(f"  right: {right_art!r}")

    return 1 if args.fail_on_match else 0


if __name__ == "__main__":
    raise SystemExit(main())
