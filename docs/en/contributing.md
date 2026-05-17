# Contributing Guide

## Core policy

This repository is not a plain archive of text art. Entries should be reusable as learning and evaluation data. Each entry should include meaning, context, plain-text paraphrase, and display metadata.

## Accepted contributions

- Text art created by the contributor
- Text art with explicit compatible permission
- CC0-compatible or public-domain-compatible material with clear provenance
- Short common expressions with contributor-written context, meaning, and paraphrase

## Not accepted by default

- Unauthorized copies from forums, social media, or websites
- Unknown-license text-art collections
- Entries containing private or identifying information
- Unreviewed discriminatory, harassing, sexual, or violent content
- Bare text-art strings without meaning or context

## Required fields

Each entry should include at least the following fields.

| Field | Description |
|---|---|
| `id` | Unique entry ID |
| `art` | Text art string |
| `art_type` | Type, such as `ascii_7bit` or `kaomoji` |
| `charset_class` | Character-set class |
| `line_count` | Number of lines |
| `context_text` | Example context |
| `intended_meaning` | Intended meaning |
| `plain_text` | Plain-text paraphrase |
| `display_requirements` | Display requirements |
| `source_type` | Source type, such as `original` |
| `license` | Example: `CC0-1.0` |
| `review_status` | Example: `draft`, `reviewed` |

## Quality criteria

Good entries satisfy the following conditions.

1. The meaning is explained, not just the raw string.
2. The context example is natural.
3. The plain-text paraphrase can be used for TTS or summarization.
4. Cultural context and display conditions are recorded when relevant.
5. Reuse rights are clear.

## Review policy

At the initial stage, small examples should be added to `data/samples.jsonl`. Once the schema and taxonomy become stable, reviewed entries can be moved into `data/reviewed/`.

Unclear entries should not be accepted as final data. Use `draft` or `needs_review` instead.
