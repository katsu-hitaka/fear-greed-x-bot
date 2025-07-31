# Fear & Greed Index X Bot

Fear & Greed Index（恐怖と欲指数）を取得し、X（旧Twitter）に自動投稿するPythonアプリケーションです。英語と日本語の両方に対応しています。

## 機能

- 📊 Fear & Greed Indexリアルタイム取得（Alternative.me API）
- 🐦 X（Twitter）への自動投稿
- 🌐 **多言語対応**（英語・日本語）
- ⏰ スケジュール投稿機能  
- 🔄 API障害時のWebスクレイピング代替手段
- 📝 詳細なログ記録

## 必要な環境

- Python 3.7以上
- X（Twitter）Developer Account
- インターネット接続

## インストール

1. **リポジトリのクローン**
```bash
git clone <repository-url>
cd fear-greed-x-bot
```

2. **仮想環境の作成と依存関係のインストール**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate     # Windows

pip install schedule requests beautifulsoup4 tweepy
```

3. **Twitter API設定**

X Developer Portalで以下の認証情報を取得：
- Bearer Token
- API Key & Secret
- Access Token & Secret

**重要**: アプリの権限を「Read and Write」に設定してください。

`src/config.py`を編集して認証情報を設定：

```python
# Twitter API Configuration
TWITTER_BEARER_TOKEN = "your_bearer_token_here"
TWITTER_API_KEY = "your_api_key_here"
TWITTER_API_SECRET = "your_api_secret_here"
TWITTER_ACCESS_TOKEN = "your_access_token_here"
TWITTER_ACCESS_TOKEN_SECRET = "your_access_token_secret_here"
```

## 使用方法

### サーバ環境での推奨設定（crontab）

crontabを使用してサーバで定期実行する場合の推奨設定：

```bash
# crontab -e で編集
# 日本語版：毎日9:00に投稿
0 9 * * * cd /path/to/fear-greed-x-bot && /usr/bin/python3 src/main.py once ja >> logs/cron.log 2>&1

# 英語版：毎日18:00に投稿  
0 18 * * * cd /path/to/fear-greed-x-bot && /usr/bin/python3 src/main.py once en >> logs/cron.log 2>&1
```

**設定手順：**
1. `crontab -e` でcrontab編集
2. 上記設定を追加（パスを実際の環境に合わせて変更）
3. `mkdir -p logs` でログディレクトリを作成
4. `chmod +x src/main.py` で実行権限を付与（必要に応じて）

**crontab使用の利点：**
- システムレベルでの実行保証
- プロセスクラッシュ時の自動復旧
- リソース効率（実行時のみプロセス起動）
- メンテナンスしやすい

### コマンドライン実行

```bash
# 接続テスト（Twitter APIとFear & Greed Index取得をテスト）
python src/main.py test

# 一度だけ実行（手動投稿）- 英語
python src/main.py once

# 一度だけ実行（手動投稿）- 日本語
python src/main.py once ja
# または
python src/main.py ja once

# 定期実行（毎日指定時刻に自動投稿）- 英語
python src/main.py schedule

# 定期実行（毎日指定時刻に自動投稿）- 日本語
python src/main.py schedule ja

# 日本語で接続テスト
python src/main.py test ja
```

### 言語オプション

- **デフォルト**: 英語でツイート投稿
- **`ja` オプション**: 日本語でツイート投稿
- 引数の順序は自由（`once ja` でも `ja once` でも同じ）

## 投稿例

### 英語版ツイート（231文字）
```
🔥 Fear & Greed Index Update 🔥

📊 Current Index: 73
📈 Status: Greed (🤑)
🕐 Last Updated: 2025-07-29 09:00:00

Investors are optimistic. Markets may be getting overheated.

#FearAndGreed #Bitcoin #Crypto #TradingView #MarketSentiment
```

### 日本語版ツイート（157文字）
```
🔥 恐怖貪欲指数 更新 🔥

📊 現在の指数: 73
📈 ステータス: 貪欲 (🤑)
🕐 データ更新: 2025-07-29 15:30:00

投資家は楽観的です。市場は過熱気味かもしれません。

#恐怖貪欲指数 #ビットコイン #仮想通貨 #投資 #マーケット #FearAndGreed

⏰ 投稿時刻: 2025-07-30 09:00
```

## 設定のカスタマイズ

`src/config.py`で以下の設定を変更可能：

#### ツイートテンプレート
```python
# 英語版テンプレート
TWEET_TEMPLATE_EN = """🔥 Fear & Greed Index Update 🔥

📊 Current Index: {index}
📈 Status: {status} ({status_emoji})
🕐 Last Updated: {timestamp}

{description}

#FearAndGreed #Bitcoin #Crypto #TradingView #MarketSentiment
"""

# 日本語版テンプレート
TWEET_TEMPLATE_JA = """🔥 恐怖貪欲指数 更新 🔥

📊 現在の指数: {index}
📈 ステータス: {status_ja} ({status_emoji})
🕐 データ更新: {timestamp}

{description}

#恐怖貪欲指数 #ビットコイン #仮想通貨 #投資 #マーケット #FearAndGreed

⏰ 投稿時刻: {current_time}
"""
```

#### スケジュール設定（Python内蔵スケジューラー使用時）
```python
TWEET_SCHEDULE_HOUR = 9    # 投稿時刻（24時間形式）
TWEET_SCHEDULE_MINUTE = 0  # 投稿分
```

**注意**: サーバ環境では上記設定より crontab を推奨します。Python内蔵スケジューラーは開発・テスト用途向けです。

#### ステータス絵文字
```python
STATUS_EMOJIS = {
    "Extreme Fear": "😱",
    "Fear": "😰", 
    "Neutral": "😐",
    "Greed": "🤑",
    "Extreme Greed": "🚀"
}
```

## ファイル構成

```
fear-greed-x-bot/
├── src/
│   ├── main.py              # メインエントリーポイント（言語選択対応）
│   ├── config.py            # 設定ファイル（英語・日本語テンプレート）
│   ├── twitter_client.py    # Twitter API クライアント
│   └── fear_greed_scraper.py # Fear & Greed Index取得（多言語対応）
├── venv/                    # Python仮想環境
├── fear_greed_bot.log      # アプリケーションログ
└── README.md               # このファイル
```

## データ取得について

### Fear & Greed Index

- **主要ソース**: Alternative.me API (`https://api.alternative.me/fng/`)
- **フォールバック**: CNNウェブサイトスクレイピング
- **更新頻度**: リアルタイム
- **指数範囲**: 0-100
  - 0-25: Extreme Fear（極度の恐怖）
  - 26-45: Fear（恐怖）
  - 46-55: Neutral（中立）
  - 56-75: Greed（欲/貪欲）
  - 76-100: Extreme Greed（極度の欲/極度の貪欲）

### API変更点

**2025年7月更新**:
- CNNのAPIエンドポイントがボット対策により利用不可になったため、Alternative.me APIに変更
- より安定したデータ取得が可能
- 商用利用可能（要Attribution）

## ログ機能

アプリケーションは`fear_greed_bot.log`ファイルに詳細なログを記録：
- API接続状況
- データ取得結果（言語別）
- ツイート投稿結果
- エラー情報

## トラブルシューティング

### よくある問題

1. **Twitter API認証エラー (403 Forbidden)**
   - Twitter Developer Portalでアプリ権限を「Read and Write」に設定
   - 権限変更後は新しいAccess TokenとSecretを再生成
   - `src/config.py`の認証情報を更新

2. **重複ツイートエラー**
   - 同じ内容のツイートは投稿できません
   - インデックス値が変わるまで待機

3. **Fear & Greed Index取得失敗**
   - インターネット接続を確認
   - Alternative.me APIの状況確認

4. **仮想環境の問題**
   - macOSの場合は仮想環境を使用してください
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

### デバッグコマンド

```bash
# 接続テスト（詳細ログ付き）
python src/main.py test

# 日本語で接続テスト
python src/main.py test ja

# ログファイルの確認
tail -f fear_greed_bot.log

# ツイートフォーマットの確認（投稿なし）
cd src && python3 -c "
from fear_greed_scraper import FearGreedScraper
from config import TWEET_TEMPLATE_EN, TWEET_TEMPLATE_JA
scraper = FearGreedScraper()
data = scraper.get_fear_greed_index()
if data:
    # 英語版
    en_data = scraper.format_tweet_data(data, 'en')
    print('English:', len(TWEET_TEMPLATE_EN.format(**en_data)), 'chars')
    # 日本語版
    ja_data = scraper.format_tweet_data(data, 'ja')
    print('Japanese:', len(TWEET_TEMPLATE_JA.format(**ja_data)), 'chars')
"
```

## API制限について

- Twitter API: 投稿制限やレート制限があります
- Alternative.me API: 無料で利用可能、商用利用時は要Attribution

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 免責事項

- 本アプリは教育・情報提供目的で作成されています
- 投資判断は自己責任で行ってください
- Alternative.meのサービス利用規約を遵守してください
- Twitter APIの利用制限に注意してください

## 貢献

プルリクエストやIssueの報告を歓迎します。

## サポート

問題や質問がある場合は、GitHubのIssueを作成してください。