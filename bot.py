print("Hello from bot!")
import sys
print(sys.version)

import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"

try:
    response = requests.get(url, timeout=10)
    print("API response status code:", response.status_code)
    print("API response body:", response.text)
except Exception as e:
    print("Error connecting to Binance API:", str(e))
