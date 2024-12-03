from uniswap_testing import get_uniswap_price_v2
from uni_token_analysis import tokens6
from fastapi import FastAPI, Request, HTTPException
from binance_price import BINANCE
from bitfinex import BITFINEX
from coinbase_price import COINBASE
from bitvavo_price import BITVAVO
from huobi_price import HUOBI
from dydx_price import DYDX
from dodo_price import get_dodo_price_v2
from app2 import COINS



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "User"}


# @app.get("/prices/uniswap/{token_a}/{token_b}/{amount}")
# def get_prices(token_a: str, token_b: str, amount=1):
#     prices = get_uniswap_price_v2(None, tokens5[token_a.upper()], tokens5[token_b.upper()], None)
#     if prices ==0:
#         raise HTTPException(status_code=404)
#     else:
#         return prices


@app.get("/prices/binance/{token_a}/{token_b}/{amount}")
def get_binance_prices(token_a: str, token_b: str, amount:int=1):
    # prices = get_uniswap_price_v2(None, tokens5[token_a.upper()], tokens5[token_b.upper()], None)
    price_a=BINANCE.get_binance_prices(f'{token_a.upper()}USDT')
    price_b=BINANCE.get_binance_prices(f'{token_b.upper()}USDT')
    if price_a is None or price_b is None:
        raise HTTPException(status_code=404)
    else:
        return (price_a), (float(price_a)/float(price_b))*amount, (f"{token_b} price in USDT is {price_b}")


@app.get("/prices/bitfinex/{token_a}/{token_b}/{amount}")
def get_bitfinex_prices(token_a: str, token_b: str, amount:int=1):
    # prices = get_uniswap_price_v2(None, tokens5[token_a.upper()], tokens5[token_b.upper()], None)
    price_a=BITFINEX.get_bitfinex_price(f't{token_a.upper()}USD')
    price_b=BITFINEX.get_bitfinex_price(f't{token_b.upper()}USD')
    if price_a is None or price_b is None:
        raise HTTPException(status_code=404)
    else:
        return (price_a), (float(price_a)/float(price_b))*amount, (f"{token_b} price in USD is {price_b}")


@app.get("/prices/coinbase/{token_a}/{token_b}/{amount}")
def get_coinbase_prices(token_a: str, token_b: str, amount:int=1):
    # prices = get_uniswap_price_v2(None, tokens5[token_a.upper()], tokens5[token_b.upper()], None)
    price_a=COINBASE.get_coinbase_prices(f'{token_a.upper()}-USD')
    price_b=COINBASE.get_coinbase_prices(f'{token_b.upper()}-USD')
    price_b_inr=COINBASE.get_coinbase_prices(f'{token_b.upper()}-INR')

    if price_a is None or price_b is None:
        raise HTTPException(status_code=404)
    else:
        return (price_a), (float(price_a)/float(price_b))*amount, (f"{token_b} price in USD is {price_b}"), (f"{token_b} price in INR is {price_b_inr}")


@app.get("/prices/bitvavo/{token_a}/{token_b}/{amount}")
def get_bitvavo_prices(token_a: str, token_b: str, amount: int=1):
    # prices = get_uniswap_price_v2(None, tokens5[token_a.upper()], tokens5[token_b.upper()], None)
    price_a=BITVAVO.get_bitvavo_prices(f'{token_a.upper()}-EUR')
    price_b=BITVAVO.get_bitvavo_prices(f'{token_b.upper()}-EUR')
    if price_a is None or price_b is None:
        raise HTTPException(status_code=404)
    else:
        return (price_a), (float(price_a)/float(price_b))*amount, (f"{token_b} price in EUR is {price_b}")


# @app.get("/prices/bitvavo/{token_a}")
# def get_bitvavo_prices(token_a: str):
#     # prices = get_uniswap_price_v2(None, tokens5[token_a.upper()], tokens5[token_b.upper()], None)
#     prices=BITVAVO.get_bitvavo_prices(f'{token_a.upper()}-EUR')
#     if prices ==None:
#         raise HTTPException(status_code=404)
#     else:
#         return f"{token_a} price in EUR is {prices}"


@app.get("/prices/huobi/{token_a}/{token_b}/{amount}")
def get_huobi_prices(token_a: str, token_b: str, amount: int=1):
    # prices = get_uniswap_price_v2(None, tokens5[token_a.upper()], tokens5[token_b.upper()], None)
    price_a=HUOBI.get_huobi_price(f'{token_a.lower()}usdt')
    price_b=HUOBI.get_huobi_price(f'{token_b.lower()}usdt')
    if price_a is None or price_b is None:
        raise HTTPException(status_code=404)
    else:
        return (price_a), (float(price_a)/float(price_b))*amount, (f"{token_b} price in USD is {price_b}")

@app.get("/prices/dydx/{token_a}/{token_b}/{amount}")
def get_dydx_prices(token_a: str, token_b: str, amount: int=1):
    # prices = get_uniswap_price_v2(None, tokens5[token_a.upper()], tokens5[token_b.upper()], None)
    price_a=DYDX.get_dydx_price(f'{token_a.upper()}-USD')
    price_b=DYDX.get_dydx_price(f'{token_b.upper()}-USD')
    if price_a is None or price_b is None:
        raise HTTPException(status_code=404)
    else:
        return (price_a), (float(price_a)/float(price_b))*amount, (f"{token_b} price in USD is {price_b}")



@app.get("/prices/uniswap/{token_a}/{token_b}/{amount}")
def get_uniswap_prices(token_a: str, token_b: str, amount: int=1):
    prices = float(get_uniswap_price_v2(None, tokens6[token_a.upper()], tokens6[token_b.upper()], amount))
    price_in_usd = float(get_uniswap_price_v2(None, tokens6[token_a.upper()], tokens6['USDC'], amount))
    if prices == 0:
        raise HTTPException(status_code=404)
    else:
        return  (price_in_usd), (float(prices))

# print(get_uniswap_prices('uni','aave', 1))

@app.get("/prices/dodo/{token_a}/{token_b}/{amount}")
def get_dodo_prices(token_a: str, token_b: str, amount: int=1):
    prices = get_dodo_price_v2(tokens6[token_a.upper()], tokens6[token_b.upper()], amount)
    price_in_usd = get_dodo_price_v2(tokens6[token_a.upper()], tokens6['USDC'], amount)
    if prices ==0:
        raise HTTPException(status_code=404)
    else:
        return (price_in_usd), (float(prices))



@app.get("/prices/pancakeswap/{token_a}/{token_b}/{amount}")
def get_pancakeswap_prices(token_a: str, token_b: str, amount:int=1):
    prices = get_pancakeswap_prices(tokens6[token_a.upper()], tokens6[token_b.upper()], amount)
    price_in_usd = get_pancakeswap_prices(tokens6[token_a.upper()], tokens6['USDC'], amount)
    if prices ==0:
        raise HTTPException(status_code=404)
    else:
        return (price_in_usd), (float(prices))


# print(get_pancakeswap_prices("uni", "aave",1))
