# open-text-art-dataset 概要

## 目的

`open-text-art-dataset` は、文字だけで作られた視覚表現を、意味・文脈・平文化・表示条件・文化的背景つきで整理するオープンデータセットです。

対象は、厳密な ASCII art だけではありません。ASCII art を一つの下位分類として扱い、ANSI art、Shift_JIS風テキストアート、顔文字、Unicode text art、単行記号表現、複数行の文字絵も対象にします。

## このプロジェクトが作るもの

- テキストアート本体
- 文脈例
- 意図された意味
- 自然文への平文化
- 感情・口調ラベル
- 誤読候補
- 表示条件メタデータ
- ライセンスと出所情報

## このプロジェクトが作らないもの

- 汎用生成AIモデル
- TTSモデル
- 画像生成モデル
- 権利不明なAA集
- 掲示板・SNS投稿の無断コピー集
- 未審査の危険表現データ

## 想定用途

- LLMのテキストアート理解評価
- TTS前処理
- スクリーンリーダー向け説明生成
- チャット要約
- 感情・口調分析
- ネット文化研究
- 日本語学習・異文化理解教材

## 基本方針

1. **データ品質を量より優先する。**
2. **自作または明示的に許諾されたデータを優先する。**
3. **意味・文脈・平文化を必ず付ける。**
4. **文字幅・改行・フォント依存などの表示条件を記録する。**
5. **文化圏を一括りにせず、メタデータで区別する。**

## 初期対象範囲

| 分類 | 内容 |
|---|---|
| `ascii_7bit` | 7-bit ASCII文字のみで作られたアート |
| `ansi_art` | ANSIエスケープや色表現を前提にしたテキストアート |
| `shift_jis_style` | 日本語掲示板文化などで発展したShift_JIS風テキストアート |
| `kaomoji` | 顔文字。例：`(｀・ω・´)` |
| `unicode_text_art` | Unicode記号・罫線・全角記号を含む文字アート |
| `single_line_symbol` | `orz`, `:-)`, `XD` などの単行表現 |
| `multi_line_text_picture` | 複数行の文字絵 |

## 最小データ例

```json
{
  "id": "text-art-000001",
  "art": "＼(^o^)／",
  "art_type": "kaomoji",
  "charset_class": "unicode_text",
  "line_count": 1,
  "context_text": "もう終わりだ＼(^o^)／",
  "intended_meaning": "自虐的な諦め",
  "plain_text": "もうだめそうです、という気持ちを冗談っぽく表している。",
  "emotion": ["despair", "humor"],
  "tone": "joking_negative",
  "possible_misreadings": ["単純な喜びとして解釈する"],
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
