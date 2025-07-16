import os
import requests
import time

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

print("Bot started!")

def check_xrp_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"
    response = requests.get(url)
    data = response.json()
    price = float(data['price'])
    return price

while True:
    price = check_xrp_price()
    print(f"Current XRP Price: {price}")
    # כאן אפשר להכניס לוגיקת מסחר פשוטה בעתיד
    time.sleep(10)  # בודק כל 10 שניות
