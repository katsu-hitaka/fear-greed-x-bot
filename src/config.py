# Configuration file for Fear & Greed Index Twitter Bot

# X (Twitter) API Configuration
TWITTER_BEARER_TOKEN = "your_bearer_token_here"
TWITTER_API_KEY = "your_api_key_here"
TWITTER_API_SECRET = "your_api_secret_here"
TWITTER_ACCESS_TOKEN = "your_access_token_here"
TWITTER_ACCESS_TOKEN_SECRET = "your_access_token_secret_here"

# Fear & Greed Index Configuration
FEAR_GREED_API_URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata/"
FEAR_GREED_FALLBACK_URL = "https://money.cnn.com/data/fear-and-greed/"

# Tweet Configuration
TWEET_TEMPLATE = """🔥 Fear & Greed Index Update 🔥

Current Index: {index}
Status: {status} ({status_emoji})
Last Updated: {timestamp}

{description}

#FearAndGreed #Bitcoin #Crypto #TradingView #MarketSentiment
"""

# Emoji mappings for different fear/greed levels
STATUS_EMOJIS = {
    "Extreme Fear": "😱",
    "Fear": "😰",
    "Neutral": "😐",
    "Greed": "🤑",
    "Extreme Greed": "🚀"
}

# Scheduling Configuration (optional)
TWEET_SCHEDULE_HOUR = 9  # Hour to tweet (24-hour format)
TWEET_SCHEDULE_MINUTE = 0  # Minute to tweet