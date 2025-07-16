print("Hello from bot!")     
import sys
print(sys.version)           
def check_xrp_price():
    url = f"{BASE_URL}/api/v3/ticker/price?symbol={TRADING_PAIR}"
    response = requests.get(url)
    print("Raw response text:", response.text)  
    try:
        data = response.json()
        print("API response:", data)  
        if 'price' not in data:
            raise Exception(f"'price' field not in response: {data}")
        price = float(data['price'])
        return price
    except Exception as e:
        print(f"Failed to parse response: {response.text}")
        raise e
