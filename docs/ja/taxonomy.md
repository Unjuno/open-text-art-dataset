# 分類表

## 文字アート分類

| 値 | 意味 | 例 |
|---|---|---|
| `ascii_7bit` | 7-bit ASCII文字だけで構成された文字アート | `:-)`, `/\_/\\` |
| `ansi_art` | ANSIエスケープや色表現を前提にした文字アート | 色付きBBS風アート |
| `shift_jis_style` | Shift_JIS風・日本語掲示板文化系の文字アート | 大型AA、モナー系など |
| `kaomoji` | 顔文字 | `(｀・ω・´)`, `m(_ _)m` |
| `unicode_text_art` | Unicode記号・罫線・全角記号を含む文字アート | `╭( ･ㅂ･)و` |
| `single_line_symbol` | 単行の記号的表現 | `orz`, `XD`, `www` |
| `multi_line_text_picture` | 複数行で形を作る文字絵 | 猫、建物、人物など |

## 文字集合分類

| 値 | 意味 |
|---|---|
| `ascii_7bit` | U+0000〜U+007FのASCII中心 |
| `extended_ascii_or_ansi` | 拡張ASCIIまたはANSI表示を想定 |
| `shift_jis` | Shift_JIS表示を想定 |
| `unicode_text` | Unicode文字を含む |
| `mixed` | 複数の文字集合・表示前提が混在 |
| `unknown` | 未確認 |

## 感情ラベル例

| 値 | 意味 |
|---|---|
| `joy` | 喜び |
| `humor` | 冗談・笑い |
| `despair` | 絶望・諦め |
| `confusion` | 困惑 |
| `confidence` | 自信・気合い |
| `apology` | 謝罪 |
| `gratitude` | 感謝 |
| `sadness` | 悲しみ |
| `anger` | 怒り |
| `surprise` | 驚き |
| `neutral` | 中立 |

## 口調ラベル例

| 値 | 意味 |
|---|---|
| `casual` | くだけた口調 |
| `polite` | 丁寧 |
| `joking` | 冗談 |
| `joking_negative` | ネガティブ内容を冗談化 |
| `sarcastic_possible` | 皮肉の可能性あり |
| `soft_negative` | 弱い否定・落ち込み |
| `positive_determined` | 前向き・気合い |
| `apologetic` | 謝罪調 |

## 文化的文脈ラベル例

| 値 | 意味 |
|---|---|
| `general_internet` | 一般的インターネット文化 |
| `japanese_internet` | 日本語圏ネット文化 |
| `bbs_culture` | 掲示板文化 |
| `chat_culture` | チャット文化 |
| `gaming_culture` | ゲーム文化 |
| `western_emoticon` | 英語圏emoticon文化 |
| `unknown` | 不明 |

## レビュー状態

| 値 | 意味 |
|---|---|
| `draft` | 下書き |
| `needs_review` | レビュー待ち |
| `reviewed` | 採用済み |
| `rejected` | 不採用 |
| `deprecated` | 非推奨・置換予定 |
