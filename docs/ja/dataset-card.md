# データセットカード

## データセット名

`open-text-art-dataset`

## 概要

文字ベースの視覚表現を、意味・文脈・平文化・表示条件・文化的背景つきで整理するオープンデータセットです。

## 対象

- ASCII art
- ANSI art
- Shift_JIS風テキストアート
- 顔文字
- Unicode text art
- 単行記号表現
- 複数行文字絵

## 意図された用途

- LLMの文字アート理解評価
- TTS前処理
- スクリーンリーダー向け説明
- チャット要約
- 感情・口調分析
- ネット文化研究
- 教材作成

## 意図しない用途

- 実在個人の識別やプロファイリング
- 出所不明AAの再配布
- 差別・嫌がらせ表現の増幅
- 文脈なしの自動モデレーション判断
- 公式辞書や法的判断の代替

## データ構造

各レコードは、少なくとも以下を含みます。

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

## データ源

初期データは、投稿者が自作した例を優先します。掲示板、SNS、Webサイト、既存AA集からの無断コピーは採用しません。

## ライセンス

初期方針では、オリジナルのデータ項目は `CC0-1.0` を目標にします。詳細は `DATA_LICENSE.md` を参照してください。

## 制限

- 意味・感情・口調のラベルには主観性があります。
- 複数行テキストアートは表示環境で崩れる可能性があります。
- 文化的意味は時代・地域・コミュニティによって変化します。
- 初期データは小規模で、網羅性を保証しません。

## 推奨される評価方法

- `art` と `context_text` から `plain_text` を生成できるか
- `intended_meaning` を分類できるか
- `possible_misreadings` を避けられるか
- 表示条件を保持できるか

## 更新方針

初期段階では `data/samples.jsonl` を中心にスキーマを検証し、十分に安定したデータのみ `data/reviewed/` に移します。
