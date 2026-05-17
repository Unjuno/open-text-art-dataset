# open-text-art-dataset

Open dataset for text-based visual expressions such as ASCII art, ANSI art, Shift_JIS-style text art, kaomoji, and Unicode text art.

文字ベースの視覚表現、すなわち ASCII art、ANSI art、Shift_JIS風テキストアート、顔文字、Unicode text art を、意味・文脈・平文化・表示条件つきで整理するオープンデータセットです。

## Documents

| Language | Overview | Dataset Card | Contributing | Taxonomy |
|---|---|---|---|---|
| Japanese | [docs/ja/overview.md](docs/ja/overview.md) | [docs/ja/dataset-card.md](docs/ja/dataset-card.md) | [docs/ja/contributing.md](docs/ja/contributing.md) | [docs/ja/taxonomy.md](docs/ja/taxonomy.md) |
| English | [docs/en/overview.md](docs/en/overview.md) | [docs/en/dataset-card.md](docs/en/dataset-card.md) | [docs/en/contributing.md](docs/en/contributing.md) | [docs/en/taxonomy.md](docs/en/taxonomy.md) |

## Purpose

This repository does **not** primarily build models. It provides reusable learning and evaluation data for downstream model builders, researchers, accessibility tools, TTS preprocessing, chat summarization, and cultural analysis.

このリポジトリは、モデル作成そのものを主目的にしません。下流のモデル開発者、研究者、アクセシビリティツール、TTS前処理、チャット要約、文化研究で使える学習・評価データを整備します。

## Initial scope

- ASCII art
- ANSI-style text art
- Shift_JIS-style text art
- Kaomoji
- Unicode text art
- Single-line symbolic expressions such as `orz`, `:-)`, `XD`
- Multi-line text pictures

## Non-goals

- Training or publishing models
- Mass-copying unknown-license text art from forums or social media
- Publishing unreviewed harmful, discriminatory, or private content
- Optimizing only for dataset size
- Treating all text art as culturally identical

## License policy

See [DATA_LICENSE.md](DATA_LICENSE.md). The default target is CC0-1.0 for original dataset entries unless stated otherwise.
