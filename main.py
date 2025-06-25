from bot import BasicBot
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the API keys from environment variables
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Initialize the bot with the keys
bot = BasicBot(API_KEY, API_SECRET)

# Example usage
bot.place_order(symbol='BTCUSDT', quantity=0.01, side='BUY')
