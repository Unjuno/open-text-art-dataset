#!/usr/bin/env python3
"""Validate dataset policy rules that complement the JSON Schema.

Hard failures are used only for deterministic, low-false-positive checks.
Warnings are used for quality signals that require human review.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "data" / "entries"
SAMPLES_PATH = ROOT / "data" / "samples.jsonl"
REVIEWED_PATH = ROOT / "data" / "reviewed" / "v0.1.jsonl"
README_PATH = ROOT / "README.md"

ALLOWED_REVIEWED_LICENSES = {"CC0-1.0"}
ALLOWED_EMOTIONS = {
    "anger",
    "apology",
    "confidence",
    "confusion",
    "despair",
    "gratitude",
    "humor",
    "joy",
    "neutral",
    "sadness",
    "surprise",
}
ALLOWED_TONES = {
    "apologetic",
    "casual",
    "joking",
    "joking_negative",
    "playful",
    "positive_determined",
    "soft_negative",
    "technical_diagram",
    "technical_status",
    "urgent",
}
ALLOWED_CULTURAL_CONTEXTS = {
    "bbs_culture",
    "chat_culture",
    "gaming_culture",
    "general_internet",
    "japanese_internet",
    "terminal_culture",
    "western_emoticon",
    "unknown",
}


def load_entry_files() -> list[tuple[Path, dict[str, Any]]]:
    entries: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(ENTRIES_DIR.glob("*.json")):
        entries.append((path, json.loads(path.read_text(encoding="utf-8"))))
    return entries


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                rows.append(json.loads(stripped))
    return rows


def readme_declared_count() -> int | None:
    text = README_PATH.read_text(encoding="utf-8")
    match = re.search(r"Current initial dataset size:\s*\*\*(\d+) reviewed entries\*\*", text)
    if not match:
        return None
    return int(match.group(1))


def contains_art_context(record: dict[str, Any]) -> bool:
    art = str(record.get("art", ""))
    context = str(record.get("context_text", ""))
    return bool(art) and art in context


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    entries = load_entry_files()
    entry_ids = [str(record.get("id", "")) for _, record in entries]
    reviewed_entries = [record for _, record in entries if record.get("review_status") == "reviewed"]

    for path, record in entries:
        record_id = str(record.get("id", ""))
        expected_filename = f"{record_id}.json"
        if path.name != expected_filename:
            failures.append(f"{path}: filename/id mismatch; expected {expected_filename}")

        if record.get("review_status") == "reviewed":
            if record.get("source_type") == "unknown":
                failures.append(f"{path}: reviewed entries must not use source_type=unknown")
            if record.get("license") not in ALLOWED_REVIEWED_LICENSES:
                failures.append(
                    f"{path}: reviewed entry has unsupported license {record.get('license')!r}"
                )
            if len(str(record.get("plain_text", ""))) < 10:
                warnings.append(f"{path}: plain_text is very short")
            if len(str(record.get("context_text", ""))) < 5:
                warnings.append(f"{path}: context_text is very short")

        if not contains_art_context(record):
            warnings.append(f"{path}: context_text does not contain the art string")

        for emotion in record.get("emotion", []):
            if emotion not in ALLOWED_EMOTIONS:
                warnings.append(f"{path}: unknown emotion label {emotion!r}")

        tone = record.get("tone")
        if tone not in ALLOWED_TONES:
            warnings.append(f"{path}: unknown tone label {tone!r}")

        for context in record.get("cultural_context", []):
            if context not in ALLOWED_CULTURAL_CONTEXTS:
                warnings.append(f"{path}: unknown cultural_context label {context!r}")

    samples = load_jsonl(SAMPLES_PATH)
    reviewed = load_jsonl(REVIEWED_PATH)

    sample_ids = [str(row.get("id", "")) for row in samples]
    reviewed_ids = [str(row.get("id", "")) for row in reviewed]
    expected_reviewed_ids = [str(row.get("id", "")) for row in reviewed_entries]

    if sample_ids != entry_ids:
        failures.append("data/samples.jsonl IDs do not match data/entries/*.json order")

    if reviewed_ids != expected_reviewed_ids:
        failures.append(
            "data/reviewed/v0.1.jsonl IDs do not match reviewed data/entries/*.json records"
        )

    declared = readme_declared_count()
    if declared is None:
        warnings.append("README.md does not declare the reviewed entry count")
    elif declared != len(reviewed_entries):
        failures.append(
            f"README reviewed count mismatch: declared={declared}, actual={len(reviewed_entries)}"
        )

    for warning in warnings:
        print(f"WARN: {warning}", file=sys.stderr)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        print(f"Dataset policy validation failed: {len(failures)} failure(s), {len(warnings)} warning(s).", file=sys.stderr)
        return 1

    print(f"Dataset policy validation passed: {len(entries)} entries, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
