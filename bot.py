def check_xrp_price():
    url = f"{BASE_URL}/api/v3/ticker/price?symbol={TRADING_PAIR}"
    response = requests.get(url)
    print("Raw response text:", response.text)  # תמיד מדפיס!
    try:
        data = response.json()
        print("API response:", data)  # אם זה כן JSON, נראה את זה
        if 'price' not in data:
            raise Exception(f"'price' field not in response: {data}")
        price = float(data['price'])
        return price
    except Exception as e:
        print(f"Failed to parse response: {response.text}")
        raise e
