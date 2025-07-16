import os

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

def main():
    print("Bot started!")
    print("API_KEY:", API_KEY)
    print("API_SECRET:", API_SECRET)

if __name__ == '__main__':
    main()
