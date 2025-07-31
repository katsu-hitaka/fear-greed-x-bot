# Configuration file for Fear & Greed Index Twitter Bot

# X (Twitter) API Configuration
TWITTER_BEARER_TOKEN = "your_bearer_token_here"
TWITTER_API_KEY = "your_api_key_here"
TWITTER_API_SECRET = "your_api_secret_here"
TWITTER_ACCESS_TOKEN = "your_access_token_here"
TWITTER_ACCESS_TOKEN_SECRET = "your_access_token_secret_here"

# Fear & Greed Index Configuration
FEAR_GREED_API_URL = "https://api.alternative.me/fng/"
FEAR_GREED_FALLBACK_URL = "https://money.cnn.com/data/fear-and-greed/"

# Tweet Configuration
TWEET_TEMPLATE_EN = """🔥 Fear & Greed Index Update 🔥

📊 Current Index: {index}
📈 Status: {status} ({status_emoji})
🕐 Last Updated: {timestamp}

{description}

#FearAndGreed #Bitcoin #Crypto #TradingView #MarketSentiment
"""

TWEET_TEMPLATE_JA = """🔥 恐怖貪欲指数 更新 🔥

📊 現在の指数: {index}
📈 ステータス: {status_ja} ({status_emoji})
🕐 データ更新: {timestamp}

{description}

#恐怖貪欲指数 #ビットコイン #仮想通貨 #投資 #マーケット #FearAndGreed

⏰ 投稿時刻: {current_time}
"""

# Default template (English)
TWEET_TEMPLATE = TWEET_TEMPLATE_EN

# Emoji mappings for different fear/greed levels
STATUS_EMOJIS = {
    "Extreme Fear": "😱",
    "Fear": "😰",
    "Neutral": "😐",
    "Greed": "🤑",
    "Extreme Greed": "🚀"
}

# Japanese status translations
STATUS_JA = {
    "Extreme Fear": "極度の恐怖",
    "Fear": "恐怖",
    "Neutral": "中立",
    "Greed": "貪欲",
    "Extreme Greed": "極度の貪欲"
}

# Scheduling Configuration (optional)
TWEET_SCHEDULE_HOUR = 9  # Hour to tweet (24-hour format)
TWEET_SCHEDULE_MINUTE = 0  # Minute to tweet