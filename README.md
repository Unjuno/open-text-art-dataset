# open-text-art-dataset

Open dataset for text-based visual expressions such as ASCII art, ANSI art, Shift_JIS-style text art, kaomoji, and Unicode text art.

文字ベースの視覚表現、すなわち ASCII art、ANSI art、Shift_JIS風テキストアート、顔文字、Unicode text art を、意味・文脈・平文化・表示条件つきで整理するオープンデータセットです。

## Status

Current initial dataset size: **20 reviewed entries**.

現在の初期データ数: **レビュー済み20件**。

Maintainer setup: [docs/maintainer/branch-protection.md](docs/maintainer/branch-protection.md)

## How to contribute

There are two contribution paths.

| Contributor type | Recommended path |
|---|---|
| Non-coders / casual contributors | Open a **New text-art entry** issue and fill in the form. |
| Coders / maintainers | Add or edit one JSON file under `data/entries/`, then open a pull request. |

Do not submit copied forum posts, copied social media posts, unknown-license archives, or private information.

参加方法は2つあります。

| 参加者 | 推奨方法 |
|---|---|
| JSONを書きたくない人 | **New text-art entry** Issueフォームから提案する |
| JSONを書ける人 | `data/entries/` に1件1JSONで追加し、Pull Requestを出す |

掲示板・SNS投稿の無断コピー、権利不明AA集、個人情報は投稿しないでください。

## Quick start

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a new entry file:

```bash
python scripts/new_entry.py
```

Build generated JSONL files:

```bash
python scripts/build_jsonl.py
```

Run all local checks:

```bash
make check
```

## Documents

| Language | Overview | Dataset Card | Contributing | Taxonomy |
|---|---|---|---|---|
| Japanese | [docs/ja/overview.md](docs/ja/overview.md) | [docs/ja/dataset-card.md](docs/ja/dataset-card.md) | [docs/ja/contributing.md](docs/ja/contributing.md) | [docs/ja/taxonomy.md](docs/ja/taxonomy.md) |
| English | [docs/en/overview.md](docs/en/overview.md) | [docs/en/dataset-card.md](docs/en/dataset-card.md) | [docs/en/contributing.md](docs/en/contributing.md) | [docs/en/taxonomy.md](docs/en/taxonomy.md) |

## Purpose

This repository does **not** primarily build models. It provides reusable learning and evaluation data for downstream model builders, researchers, accessibility tools, TTS preprocessing, chat summarization, and cultural analysis.

このリポジトリは、モデル作成そのものを主目的にしません。下流のモデル開発者、研究者、アクセシビリティツール、TTS前処理、チャット要約、文化研究で使える学習・評価データを整備します。

## Editing model

Source-of-truth entries are stored as one JSON file per entry:

```text
data/entries/text-art-000001.json
```

Generated artifacts:

```text
data/samples.jsonl
data/reviewed/v0.1.jsonl
```

Do **not** manually edit generated JSONL files. Edit `data/entries/*.json`, then run:

```bash
python scripts/build_jsonl.py
```

Validate dataset files:

```bash
python scripts/validate_entries.py
python scripts/validate_jsonl.py data/samples.jsonl data/reviewed/v0.1.jsonl
python scripts/report_near_duplicates.py
```

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
