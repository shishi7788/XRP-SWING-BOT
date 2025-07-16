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

TRADE_AMOUNT = float(os.getenv('TRADE_AMOUNT', '20'))
MAX_TRADES = int(os.getenv('MAX_TRADES', '3'))
SELL_PCT = float(os.getenv('SELL_PCT', '0.7'))
RSI_PERIOD = 14
RSI_BUY = 30
RSI_SELL = 50
DROP_24H = 2
PROFIT_TARGET = 0.04
STOP_LOSS = -0.03
MAX_HOURS = 48

def sign_request(params):
    query_string = urlencode(params)
    signature = hmac.new(API_SECRET.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    params['signature'] = signature
    return params

def check_xrp_price():
    url = f"{BASE_URL}/api/v3/ticker/price?symbol={TRADING_PAIR}"
    response = requests.get(url)
    data = response.json()
    print("API response:", data)
    price = float(data['price'])
    return price

def main():
    while True:
        try:
            price = check_xrp_price()
            print(f"Current {TRADING_PAIR} price: {price}")
            # Add your trading logic here

        except Exception as e:
            print("Error:", e)
        
        time.sleep(60)  # Check price every 60 seconds

if __name__ == "__main__":
    main()
