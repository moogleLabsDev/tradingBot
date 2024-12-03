import requests


def fetch_token_prices(api_key, secret_key, symbols):
    url = "https://api.leocoinexchange.com/v1/ticker"
    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY': api_key,
        'X-API-SECRET': secret_key
    }

    prices = {}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        for symbol in symbols:
            if symbol in data:
                prices[symbol] = data[symbol]['last_price']
            else:
                prices[symbol] = None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        for symbol in symbols:
            prices[symbol] = None

    return prices


# Replace with your actual API keys and symbols
api_key = 'your_api_key'
secret_key = 'your_secret_key'
symbols = ['BTCUSD', 'ETHUSD', 'AAVEUSD', 'UNIUSD', 'LINKUSD']

# Fetch prices
prices = fetch_token_prices(api_key, secret_key, symbols)

# Print prices
for symbol, price in prices.items():
    if price:
        print(f"The current price of {symbol} is ${price}")
    else:
        print(f"Failed to fetch the price for {symbol}")
