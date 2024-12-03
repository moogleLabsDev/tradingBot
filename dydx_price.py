import requests

class DYDX():
    def get_dydx_price(token_pair):
        # URL for dYdX markets API
        url = 'https://api.dydx.exchange/v3/markets'

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        data = response.json()

        # Fetch and print the price for the specific token pair
        market = (data['markets'].get(token_pair.upper()))
        if market:
            return market['indexPrice']
        else:
            return None

# print(DYDX.get_dydx_price('ETH-USD'))


def fetch_token_prices():
    # URL for dYdX markets API
    url = 'https://api.dydx.exchange/v3/markets'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    data = response.json()

    # Print token prices
    for market in data['markets'].values():
        print(f"Token: {market['market']}, Price: {market['indexPrice']}")

# fetch_token_prices()