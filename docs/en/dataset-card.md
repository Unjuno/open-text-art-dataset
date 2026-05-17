# Dataset Card

## Dataset name

`open-text-art-dataset`

## Summary

An open dataset for text-based visual expressions with meaning, context, plain-text paraphrases, display requirements, and cultural metadata.

## Scope

- ASCII art
- ANSI art
- Shift_JIS-style text art
- Kaomoji
- Unicode text art
- Single-line symbolic expressions
- Multi-line text pictures

## Intended uses

- Evaluation of LLM text-art understanding
- TTS preprocessing
- Screen-reader descriptions
- Chat summarization
- Emotion and tone analysis
- Internet culture research
- Educational materials

## Out-of-scope uses

- Personal identification or profiling
- Redistribution of unknown-license text art
- Amplification of discriminatory or harassing expressions
- Context-free automated moderation decisions
- Replacement for official dictionaries or legal determinations

## Data structure

Each record should include at least:

- `id`
- `art`
- `art_type`
- `charset_class`
- `line_count`
- `context_text`
- `intended_meaning`
- `plain_text`
- `emotion`
- `tone`
- `possible_misreadings`
- `display_requirements`
- `cultural_context`
- `source_type`
- `license`
- `review_status`

## Data sources

Initial data should prioritize original entries created by contributors. Unauthorized copies from forums, social media, websites, or existing text-art collections are not accepted by default.

## License

The initial target license for original dataset entries is `CC0-1.0`. See `DATA_LICENSE.md` for details.

## Limitations

- Meaning, emotion, and tone labels are partly subjective.
- Multi-line text art can break across display environments.
- Cultural meanings change across time, region, and community.
- Early releases are small and not exhaustive.

## Recommended evaluation tasks

- Generate `plain_text` from `art` and `context_text`.
- Classify `intended_meaning`.
- Avoid `possible_misreadings`.
- Preserve display requirements.

## Update policy

At the initial stage, `data/samples.jsonl` is used to test the schema. Only sufficiently stable and reviewed entries should be moved into `data/reviewed/`.
