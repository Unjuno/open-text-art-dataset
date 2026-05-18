#!/usr/bin/env python3
"""Update README reviewed-entry count from data/entries/*.json."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "data" / "entries"
README_PATH = ROOT / "README.md"

EN_PATTERN = re.compile(r"Current initial dataset size: \*\*\d+ reviewed entries\*\*\.")
JA_PATTERN = re.compile(r"現在の初期データ数: \*\*レビュー済み\d+件\*\*。")


def reviewed_count() -> int:
    count = 0
    for path in sorted(ENTRIES_DIR.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("review_status") == "reviewed":
            count += 1
    return count


def main() -> int:
    count = reviewed_count()
    readme = README_PATH.read_text(encoding="utf-8")
    readme = EN_PATTERN.sub(
        f"Current initial dataset size: **{count} reviewed entries**.", readme
    )
    readme = JA_PATTERN.sub(
        f"現在の初期データ数: **レビュー済み{count}件**。", readme
    )
    README_PATH.write_text(readme, encoding="utf-8")
    print(f"Updated README reviewed-entry count to {count}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
