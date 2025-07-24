import tweepy
import logging
from config import (
    TWITTER_BEARER_TOKEN,
    TWITTER_API_KEY, 
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)

class TwitterClient:
    def __init__(self):
        self.client = None
        self.setup_twitter_client()
    
    def setup_twitter_client(self):
        """Initialize Twitter API v2 client with authentication"""
        try:
            self.client = tweepy.Client(
                bearer_token=TWITTER_BEARER_TOKEN,
                consumer_key=TWITTER_API_KEY,
                consumer_secret=TWITTER_API_SECRET,
                access_token=TWITTER_ACCESS_TOKEN,
                access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
                wait_on_rate_limit=True
            )
            
            # Test authentication
            me = self.client.get_me()
            if me.data:
                logging.info(f"Twitter authentication successful. Connected as: @{me.data.username}")
            else:
                logging.error("Failed to authenticate with Twitter API")
                
        except Exception as e:
            logging.error(f"Error setting up Twitter client: {e}")
            self.client = None
    
    def tweet(self, text):
        """Post a tweet"""
        if not self.client:
            logging.error("Twitter client not initialized")
            return False
        
        try:
            if len(text) > 280:
                logging.warning(f"Tweet text too long ({len(text)} characters). Truncating...")
                text = text[:277] + "..."
            
            response = self.client.create_tweet(text=text)
            
            if response.data:
                tweet_id = response.data['id']
                logging.info(f"Tweet posted successfully: https://twitter.com/i/web/status/{tweet_id}")
                return True
            else:
                logging.error("Failed to post tweet - no response data")
                return False
                
        except tweepy.TooManyRequests:
            logging.error("Rate limit exceeded. Tweet not posted.")
            return False
        except tweepy.Unauthorized:
            logging.error("Unauthorized. Check your Twitter API credentials.")
            return False
        except Exception as e:
            logging.error(f"Error posting tweet: {e}")
            return False
    
    def is_authenticated(self):
        """Check if Twitter client is properly authenticated"""
        return self.client is not None