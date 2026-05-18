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

Regenerate JSONL artifacts and README count:

```bash
make sync
```

Run local checks:

```bash
make check
```

CI validates entries, checks duplicate IDs, checks duplicate `art` strings, checks `line_count`, rebuilds JSONL artifacts, validates dataset policy rules, reports near-duplicate candidates, and fails if generated artifacts are not committed.

## Normal data-entry PR scope

For normal dataset contributions, keep the PR focused on dataset entries.

Allowed normal data-entry changes:

```text
data/entries/text-art-*.json
data/samples.jsonl
data/reviewed/v0.1.jsonl
README.md dataset count
```

`data/samples.jsonl`, `data/reviewed/v0.1.jsonl`, and the README dataset count should change only as the result of running:

```bash
make sync
```

Do not mix normal data-entry changes with changes to:

```text
.github/**
scripts/**
schemas/**
DATA_LICENSE.md
LICENSE*
```

Open a separate maintainer-discussion PR for workflow, script, schema, or license-policy changes.

通常のデータ追加PRでは、PRをデータ項目の追加・修正に集中させてください。

通常許可される変更範囲：

```text
data/entries/text-art-*.json
data/samples.jsonl
data/reviewed/v0.1.jsonl
README.md の件数表示
```

`data/samples.jsonl`、`data/reviewed/v0.1.jsonl`、README件数は `make sync` の結果としてのみ変更してください。

通常のデータ追加PRでは、以下を混ぜないでください。

```text
.github/**
scripts/**
schemas/**
DATA_LICENSE.md
LICENSE*
```

workflow、script、schema、license policy の変更は、別PRとして管理者向けに提案してください。

## Generated file automation

Generated files are:

```text
data/samples.jsonl
data/reviewed/v0.1.jsonl
README.md dataset count
```

For maintainers pushing directly to `main`, the `Sync generated files` workflow can commit generated updates automatically after `data/entries/` changes.

For pull requests, the `Check generated files on PR` workflow runs `make sync`. If generated files are stale, it fails the check and adds a PR comment or workflow summary telling the contributor to run:

```bash
make sync
make check
```

External fork pull requests may not always allow bot comments, but the workflow summary and failed check still show the required command.

## Automated policy checks

The dataset policy validator fails on deterministic problems such as:

- filename and `id` mismatch
- reviewed entry with `source_type: unknown`
- reviewed entry with unsupported license
- generated JSONL IDs not matching source entries
- README reviewed-entry count mismatch

It also emits warnings for quality signals that require human judgment, such as:

- `context_text` not containing the `art` string
- very short `plain_text`
- unknown `emotion`, `tone`, or `cultural_context` labels

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
