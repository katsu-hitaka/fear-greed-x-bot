# Fear & Greed Index Twitter Bot

CNNのFear & Greed Index（恐怖と欲指数）を取得し、X（旧Twitter）に自動投稿するPythonアプリケーションです。

## 機能

- 📊 CNNのFear & Greed Indexリアルタイム取得
- 🐦 X（Twitter）への自動投稿
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

2. **依存関係のインストール**
```bash
pip install -r requirements.txt
```

3. **Twitter API設定**

X Developer Portalで以下の認証情報を取得：
- Bearer Token
- API Key & Secret
- Access Token & Secret

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

### コマンドライン実行

```bash
# 接続テスト（Twitter APIとFear & Greed Index取得をテスト）
python src/main.py test

# 一度だけ実行（手動投稿）
python src/main.py once

# 定期実行（毎日指定時刻に自動投稿）
python src/main.py schedule
```

### 設定のカスタマイズ

`src/config.py`で以下の設定を変更可能：

#### ツイート内容
```python
TWEET_TEMPLATE = """🔥 Fear & Greed Index Update 🔥

Current Index: {index}
Status: {status} ({status_emoji})
Last Updated: {timestamp}

{description}

#FearAndGreed #Bitcoin #Crypto #TradingView #MarketSentiment
"""
```

#### スケジュール設定
```python
TWEET_SCHEDULE_HOUR = 9    # 投稿時刻（24時間形式）
TWEET_SCHEDULE_MINUTE = 0  # 投稿分
```

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
│   ├── main.py              # メインエントリーポイント
│   ├── config.py            # 設定ファイル（要編集）
│   ├── twitter_client.py    # Twitter API クライアント
│   └── fear_greed_scraper.py # Fear & Greed Index取得
├── requirements.txt         # Python依存関係
├── .env.example            # 環境変数例
└── README.md               # このファイル
```

## データ取得について

### Fear & Greed Index

- **主要ソース**: CNN Production API
- **フォールバック**: CNNウェブサイトスクレイピング
- **更新頻度**: リアルタイム
- **指数範囲**: 0-100
  - 0-25: Extreme Fear（極度の恐怖）
  - 26-45: Fear（恐怖）
  - 46-55: Neutral（中立）
  - 56-75: Greed（欲）
  - 76-100: Extreme Greed（極度の欲）

### Twitter投稿フォーマット

投稿される内容例：
```
🔥 Fear & Greed Index Update 🔥

Current Index: 32
Status: Fear 😰
Last Updated: 2024-01-15 09:00:00

Investors are worried. Markets may be oversold.

#FearAndGreed #Bitcoin #Crypto #TradingView #MarketSentiment
```

## ログ機能

アプリケーションは`fear_greed_bot.log`ファイルに詳細なログを記録：
- API接続状況
- データ取得結果
- ツイート投稿結果
- エラー情報

## トラブルシューティング

### よくある問題

1. **Twitter API認証エラー**
   - `src/config.py`の認証情報を確認
   - Twitter Developer Portalで権限設定を確認

2. **Fear & Greed Index取得失敗**
   - インターネット接続を確認
   - CNNのサイトアクセス制限の可能性

3. **文字数制限エラー**
   - ツイートテンプレートが280文字を超えている
   - `TWEET_TEMPLATE`を短縮

### デバッグコマンド

```bash
# 詳細ログ付きで実行
python src/main.py test

# ログファイルの確認
tail -f fear_greed_bot.log
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 免責事項

- 本アプリは教育・情報提供目的で作成されています
- 投資判断は自己責任で行ってください
- CNNのサービス利用規約を遵守してください
- Twitter APIの利用制限に注意してください

## 貢献

プルリクエストやIssueの報告を歓迎します。

## サポート

問題や質問がある場合は、GitHubのIssueを作成してください。