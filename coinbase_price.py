import requests

class COINBASE():
    def get_coinbase_prices(symbol):
        url = "https://api.coinbase.com/v2/prices/{}/spot"
        # prices = {}


        response = requests.get(url.format(symbol))
        if response.status_code == 200:
            data = response.json()
            # prices[symbol] = data['data']['amount']
            prices = data['data']['amount']
        else:
            prices = None

        return prices


# Define the symbols you want to fetch prices for
    symbols = ['BTC-USD', 'ETH-USD', 'AAVE-USD', 'UNI-USD', 'LINK-USD']

# Get the prices
prices = COINBASE.get_coinbase_prices(COINBASE.symbols)

# Print the prices
# for symbol, price in prices.items():
#     if price:
#         print(f"The current price of {symbol} is ${price}")
#     else:
#         print(f"Failed to fetch the price for {symbol}")

# print(COINBASE.get_coinbase_prices("BTC-USD"))