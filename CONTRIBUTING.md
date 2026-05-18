# Contributing / 投稿について

This repository accepts text-art dataset entries only when they are reusable as learning or evaluation data.

このリポジトリでは、学習・評価データとして再利用できる形のテキストアート項目だけを受け入れます。

## Source-of-truth policy

Do not manually edit generated JSONL artifacts:

```text
data/samples.jsonl
data/reviewed/v0.1.jsonl
```

Edit or add one JSON file per entry instead:

```text
data/entries/*.json
```

Create a new entry template:

```bash
python scripts/new_entry.py
```

Regenerate JSONL artifacts:

```bash
python scripts/build_jsonl.py
```

Run local checks:

```bash
make check
```

CI validates entries, checks duplicate IDs, checks duplicate `art` strings, checks `line_count`, rebuilds JSONL artifacts, reports near-duplicate candidates, and fails if generated artifacts are not committed.

## English

Read the full English guide:

- [docs/en/contributing.md](docs/en/contributing.md)

Minimum requirements:

- Submit only original or clearly licensed entries.
- Include meaning, context, plain-text paraphrase, display requirements, and license metadata.
- Do not submit copied forum posts, copied social media posts, unknown-license archives, or private information.
- Use per-entry JSON files under `data/entries/` and follow [schemas/entry.schema.json](schemas/entry.schema.json).

## 日本語

詳しい日本語ガイドはこちらです。

- [docs/ja/contributing.md](docs/ja/contributing.md)

最低条件：

- 自作または明確に許諾されたデータだけを投稿する。
- 意味、文脈、平文化、表示条件、ライセンス情報を含める。
- 掲示板・SNS投稿の無断コピー、権利不明AA集、個人情報を投稿しない。
- `data/entries/` 以下の1件1JSON形式で、[schemas/entry.schema.json](schemas/entry.schema.json) に従う。
