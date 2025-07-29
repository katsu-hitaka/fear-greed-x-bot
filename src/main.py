import logging
import schedule
import time
from datetime import datetime
from twitter_client import TwitterClient
from fear_greed_scraper import FearGreedScraper
from config import TWEET_TEMPLATE, TWEET_TEMPLATE_EN, TWEET_TEMPLATE_JA, TWEET_SCHEDULE_HOUR, TWEET_SCHEDULE_MINUTE

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fear_greed_bot.log'),
        logging.StreamHandler()
    ]
)

class FearGreedBot:
    def __init__(self, language='en'):
        self.twitter_client = TwitterClient()
        self.fear_greed_scraper = FearGreedScraper()
        self.language = language
        
    def post_fear_greed_update(self):
        """Main function to fetch Fear & Greed data and post to Twitter"""
        logging.info("Starting Fear & Greed Index update...")
        
        # Check Twitter authentication
        if not self.twitter_client.is_authenticated():
            logging.error("Twitter client not authenticated. Aborting update.")
            return False
        
        # Fetch Fear & Greed Index data
        fear_greed_data = self.fear_greed_scraper.get_fear_greed_index()
        if not fear_greed_data:
            logging.error("Failed to fetch Fear & Greed Index data")
            return False
        
        # Format data for tweet
        tweet_data = self.fear_greed_scraper.format_tweet_data(fear_greed_data, self.language)
        if not tweet_data:
            logging.error("Failed to format tweet data")
            return False
        
        # Select appropriate template based on language
        if self.language == 'ja':
            tweet_template = TWEET_TEMPLATE_JA
        else:
            tweet_template = TWEET_TEMPLATE_EN
            
        # Create tweet text
        tweet_text = tweet_template.format(**tweet_data)
        
        logging.info(f"Posting tweet: Current Index = {tweet_data['index']}, Status = {tweet_data['status']}")
        
        # Post tweet
        success = self.twitter_client.tweet(tweet_text)
        
        if success:
            logging.info("Fear & Greed Index update posted successfully!")
        else:
            logging.error("Failed to post Fear & Greed Index update")
        
        return success
    
    def run_once(self):
        """Run the bot once (for testing or manual execution)"""
        return self.post_fear_greed_update()
    
    def run_scheduled(self):
        """Run the bot on a schedule"""
        logging.info(f"Scheduling daily tweets at {TWEET_SCHEDULE_HOUR:02d}:{TWEET_SCHEDULE_MINUTE:02d}")
        
        # Schedule the job
        schedule.every().day.at(f"{TWEET_SCHEDULE_HOUR:02d}:{TWEET_SCHEDULE_MINUTE:02d}").do(
            self.post_fear_greed_update
        )
        
        logging.info("Bot started. Waiting for scheduled time...")
        
        # Keep the script running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    def test_connection(self):
        """Test both Twitter and Fear & Greed connections"""
        logging.info("Testing connections...")
        
        # Test Twitter
        if self.twitter_client.is_authenticated():
            logging.info("✅ Twitter connection: OK")
        else:
            logging.error("❌ Twitter connection: FAILED")
        
        # Test Fear & Greed data
        data = self.fear_greed_scraper.get_fear_greed_index()
        if data:
            logging.info(f"✅ Fear & Greed data: OK (Current: {data['index']} - {data['status']})")
        else:
            logging.error("❌ Fear & Greed data: FAILED")
        
        return self.twitter_client.is_authenticated() and data is not None

def main():
    """Main entry point"""
    import sys
    
    # Parse arguments
    language = 'en'  # default
    command = None
    
    for arg in sys.argv[1:]:
        if arg.lower() == 'ja':
            language = 'ja'
        elif arg.lower() in ['test', 'once', 'schedule']:
            command = arg.lower()
    
    bot = FearGreedBot(language=language)
    
    if command == "test":
        # Test connections
        bot.test_connection()
    elif command == "once":
        # Run once
        bot.run_once()
    elif command == "schedule":
        # Run on schedule
        bot.run_scheduled()
    elif len(sys.argv) > 1 and not any(arg in ['ja'] for arg in sys.argv[1:]):
        print("Usage: python main.py [test|once|schedule] [ja]")
        print("  test     - Test Twitter and Fear & Greed connections")
        print("  once     - Post Fear & Greed update once")
        print("  schedule - Run on daily schedule")
        print("  ja       - Use Japanese language (can be combined with commands)")
        print("")
        print("Examples:")
        print("  python main.py once     - Post once in English")
        print("  python main.py once ja  - Post once in Japanese")
        print("  python main.py ja once  - Post once in Japanese")
    else:
        # Default: run once
        lang_msg = "Japanese" if language == 'ja' else "English"
        print(f"Running Fear & Greed update once in {lang_msg}...")
        bot.run_once()

if __name__ == "__main__":
    main()