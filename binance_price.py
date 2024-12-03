import requests

class BINANCE():
    def get_binance_prices(symbol):
        url = "https://api.binance.com/api/v3/ticker/price"
        # prices = {}

        # for symbol in symbols:
        response = requests.get(url, params={'symbol': symbol})
        if response.status_code == 200:
            data = response.json()
            price = data['price']
        else:
            price = None

        return price


    # Define the symbols you want to fetch prices for
    # Note: Binance uses different symbol formats, e.g., BTCUSDT for BTC/USD
    symbols = ['BTCUSDT', 'ETHUSDT', 'AAVEUSDT', 'UNIUSDT', 'LINKUSDT']

    # Get the prices
    # prices = get_binance_prices(symbols)

# # Print the prices
# for symbol, price in BINANCE.prices.items():
#     if price:
#         print(f"The current price of {symbol} is ${price}")
#     else:
#         print(f"Failed to fetch the price for {symbol}")
