import requests
import json
import re
import logging
from datetime import datetime
from bs4 import BeautifulSoup
from config import FEAR_GREED_API_URL, FEAR_GREED_FALLBACK_URL, STATUS_EMOJIS

class FearGreedScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get_fear_greed_index(self):
        """Get current Fear & Greed Index data"""
        try:
            # Try API endpoint first
            data = self._fetch_from_api()
            if data:
                return data
            
            # Fallback to web scraping
            logging.info("API failed, falling back to web scraping...")
            return self._fetch_from_web()
            
        except Exception as e:
            logging.error(f"Error fetching Fear & Greed Index: {e}")
            return None
    
    def _fetch_from_api(self):
        """Fetch data from CNN's API endpoint"""
        try:
            response = self.session.get(FEAR_GREED_API_URL, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if 'fear_and_greed' in data:
                current_data = data['fear_and_greed']
                if current_data:
                    latest = current_data[0]  # Most recent data
                    return {
                        'index': int(latest['y']),
                        'status': self._get_status_from_index(int(latest['y'])),
                        'timestamp': latest['x'],
                        'source': 'API'
                    }
        except Exception as e:
            logging.warning(f"API fetch failed: {e}")
            return None
    
    def _fetch_from_web(self):
        """Fallback web scraping method"""
        try:
            response = self.session.get(FEAR_GREED_FALLBACK_URL, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for the fear and greed index value
            index_element = soup.find('div', class_='modFearGreedMeter')
            if not index_element:
                # Try alternative selectors
                index_element = soup.find('span', class_='wsod_fgIndex')
            
            if index_element:
                # Extract index value
                index_text = index_element.get_text(strip=True)
                index_match = re.search(r'(\d+)', index_text)
                
                if index_match:
                    index_value = int(index_match.group(1))
                    status = self._get_status_from_index(index_value)
                    
                    return {
                        'index': index_value,
                        'status': status,
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'source': 'Web Scraping'
                    }
            
            logging.error("Could not find Fear & Greed Index data on webpage")
            return None
            
        except Exception as e:
            logging.error(f"Web scraping failed: {e}")
            return None
    
    def _get_status_from_index(self, index_value):
        """Convert index value to status text"""
        if index_value <= 25:
            return "Extreme Fear"
        elif index_value <= 45:
            return "Fear"
        elif index_value <= 55:
            return "Neutral"
        elif index_value <= 75:
            return "Greed"
        else:
            return "Extreme Greed"
    
    def get_status_emoji(self, status):
        """Get emoji for the given status"""
        return STATUS_EMOJIS.get(status, "📊")
    
    def get_status_description(self, status):
        """Get description for the given status"""
        descriptions = {
            "Extreme Fear": "Markets are in panic mode. This could be a buying opportunity.",
            "Fear": "Investors are worried. Markets may be oversold.",
            "Neutral": "Markets are balanced between fear and greed.",
            "Greed": "Investors are optimistic. Markets may be getting overheated.",
            "Extreme Greed": "Markets are euphoric. This could signal a correction ahead."
        }
        return descriptions.get(status, "Market sentiment indicator")
    
    def format_tweet_data(self, data):
        """Format Fear & Greed data for tweeting"""
        if not data:
            return None
        
        status_emoji = self.get_status_emoji(data['status'])
        description = self.get_status_description(data['status'])
        
        return {
            'index': data['index'],
            'status': data['status'],
            'status_emoji': status_emoji,
            'timestamp': data['timestamp'],
            'description': description,
            'source': data.get('source', 'Unknown')
        }