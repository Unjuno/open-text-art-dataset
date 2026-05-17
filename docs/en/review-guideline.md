# Review Guideline

## Purpose

This document defines the review criteria for deciding whether a submitted text-art entry can be accepted as reusable learning or evaluation data.

## Review dimensions

| Dimension | What to check |
|---|---|
| License | Does the contributor have the right to redistribute the entry? |
| Context | Is the example context natural? |
| Meaning | Is the intended meaning sufficiently explained? |
| Plain-text paraphrase | Can it be used for TTS or summarization? |
| Display requirements | Are line breaks, monospace assumptions, and font dependencies documented when needed? |
| Cultural context | Are the relevant cultural labels included? |
| JSON structure | Does the entry match the schema? |
| Safety | Does the entry avoid personal data, discriminatory content, or unsafe material? |

## Entries more likely to be accepted

- Original entries
- Natural context examples
- Clear paraphrases
- Meaning explained or ambiguity documented
- Display requirements documented

## Entries less likely to be accepted

- Unknown provenance
- Missing meaning explanations
- Missing cultural context
- Severe display breakage
- Bare strings without context

## Recommended review statuses

| Status | Meaning |
|---|---|
| `draft` | Newly submitted |
| `needs_review` | Waiting for review |
| `reviewed` | Accepted |
| `rejected` | Rejected |
| `deprecated` | Deprecated |
