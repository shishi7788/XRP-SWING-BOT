import time
import requests
import hmac
import hashlib
import os
from urllib.parse import urlencode
from datetime import datetime, timedelta

print("Bot started!")

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')
BASE_URL = 'https://api.binance.com'
TRADING_PAIR = 'XRPUSDT'

def check_xrp_price():
    url = f"{BASE_URL}/api/v3/ticker/price?symbol={TRADING_PAIR}"
    response = requests.get(url)
    try:
        data = response.json()
        print("Raw response:", data)  # <-- This will show exactly what Binance API returns
    except Exception as e:
        print("Failed to parse response:", response.text)
        raise e
    if 'price' not in data:
        raise Exception(f"Field 'price' not found in API response: {data}")
    price = float(data['price'])
    return price

def main():
    while True:
        try:
            price = check_xrp_price()
            print(f"Current {TRADING_PAIR} price: {price}")
            # Add your trading logic here!
        except Exception as e:
            print("Error:", e)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
