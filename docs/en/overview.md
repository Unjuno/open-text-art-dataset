# open-text-art-dataset Overview

## Purpose

`open-text-art-dataset` is an open dataset for text-based visual expressions with meaning, context, plain-text paraphrases, display requirements, and cultural metadata.

The project is not limited to strict ASCII art. ASCII art is treated as one subtype. The broader scope includes ANSI art, Shift_JIS-style text art, kaomoji, Unicode text art, single-line symbolic expressions, and multi-line text pictures.

## What this project creates

- Text art entries
- Context examples
- Intended meanings
- Plain-text paraphrases
- Emotion and tone labels
- Possible misreadings
- Display requirement metadata
- Source and license metadata

## What this project does not create

- General-purpose generative AI models
- TTS models
- Image generation models
- Unknown-license text art archives
- Unauthorized copies from forums or social media
- Unreviewed harmful-expression datasets

## Intended uses

- Evaluation of LLM text-art understanding
- TTS preprocessing
- Screen-reader descriptions
- Chat summarization
- Emotion and tone analysis
- Internet culture research
- Language and cross-cultural learning materials

## Core principles

1. **Prefer data quality over volume.**
2. **Prefer original or explicitly licensed entries.**
3. **Always include meaning, context, and plain-text paraphrases.**
4. **Record display requirements such as width, line breaks, and font dependency.**
5. **Do not treat all text-art cultures as identical; record cultural context as metadata.**

## Initial scope

| Class | Description |
|---|---|
| `ascii_7bit` | Art made only from 7-bit ASCII characters |
| `ansi_art` | Text art that assumes ANSI escape sequences or color styling |
| `shift_jis_style` | Shift_JIS-style text art associated with Japanese forum culture and related contexts |
| `kaomoji` | Face-like text expressions such as `(｀・ω・´)` |
| `unicode_text_art` | Text art using Unicode symbols, box drawing characters, or full-width symbols |
| `single_line_symbol` | Single-line expressions such as `orz`, `:-)`, or `XD` |
| `multi_line_text_picture` | Multi-line text pictures |

## Minimal entry example

```json
{
  "id": "text-art-000001",
  "art": "＼(^o^)／",
  "art_type": "kaomoji",
  "charset_class": "unicode_text",
  "line_count": 1,
  "context_text": "もう終わりだ＼(^o^)／",
  "intended_meaning": "comic despair",
  "plain_text": "The speaker jokingly expresses that the situation seems hopeless.",
  "emotion": ["despair", "humor"],
  "tone": "joking_negative",
  "possible_misreadings": ["Interpreting it as simple joy"],
  "display_requirements": {
    "monospace_required": false,
    "known_font_dependency": false,
    "preserve_line_breaks": true
  },
  "cultural_context": ["japanese_internet"],
  "source_type": "original",
  "license": "CC0-1.0",
  "review_status": "reviewed"
}
```
