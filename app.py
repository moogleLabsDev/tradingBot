import requests
import json
from datetime import datetime
from web3 import Web3, HTTPProvider
from termcolor import colored
import time
import ccxt

# Constants
PRIVATE_KEY = "dcacdff3fce35db890ee008b69d16baedfcffade14396c71beba1586feaccf11"
MORALIS_APIKEY = "8RzKHVWr03FVYji5VKFZFxLh5e5FQ9PZPqeUDtwYIGnZkPz1ounQkUoGLgSakDlo"
DODO_APIKEY = "b13f92d15210daeefd"
DODO_API_ENDPOINT = "https://api.dodoex.io/route-service/developer/getdodoroute"
RPC_URL = "https://bsc-dataseed4.bnbchain.org"
alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/UcLnaPDIR4S2rplgaMDMe_g0VmTt4sJ1"
ROUTES = ["pancakeswap_v2","uniswap_v2","dodo_dex"]
# ROUTES = ["uniswap_v2"]



W3 = Web3(HTTPProvider(RPC_URL))
# Uniswap configuration
uniswap_router_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
uniswap_factory_address = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
uniswap_abi_url = "https://api.etherscan.io/api?module=contract&action=getabi&address=" + uniswap_router_address
response = requests.get(uniswap_abi_url)
uniswap_abi = response.json()["result"]
with open('factory.json') as f:
    factory_abi = (json.load(f))['result']

fact_contr=W3.eth.contract(address=uniswap_factory_address, abi=factory_abi)




COINS = {
    "usdt": "0x55d398326f99059fF775485246999027B3197955",
    "weth": "0x4DB5a66E937A9F4473fA95b1cAF1d1E1D62E29EA",
    "eth": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
    "btcb": "0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c",
    "usdc": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
    "fxs": "0xe48A3d7d0Bc88d552f730B62c006bC925eadB9eE",
    "mc": "0x949D48EcA67b17269629c7194F4b727d4Ef9E5d6",
    "frax": "0x90C97F71E18723b0Cf0dfa30ee176Ab653E89F40",
    "dai": "0x1AF3F329e8BE154074D8769D1FFa4eE058B1DBc3",
    "woo": "0x4691937a7508860F876c9c0a2a617E7d9E945D4B",
    "uni": "0xBf5140A22578168FD562DCcF235E5D43A02ce9B1",
    "super": "0x51BA0b044d96C3aBfcA52B64D733603CCC4F0d4D",
    "wbnb": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
    "cell": "0xd98438889Ae7364c7E2A3540547Fad042FB24642",
    "sand": "0x67b725d7e342d7B611fa85e859Df9697D9378B2e",
    "shib": "0x2859e4544C4bB03966803b044A93563Bd2D0DD4D",
    'bel': '0x8443f091997f06a61670B735ED92734F5628692F',
    'axs': '0x715D400F88C167884bbCc41C5FeA407ed4D2f8A0',
    'ach': '0xBc7d6B50616989655AfD682fb42743507003056D',
    "cake": "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82",
    "8pay": "0xFeea0bDd3D07eb6FE305938878C0caDBFa169042",
    "aave": "0xfb6115445Bff7b52FeB98650C87f44907E58f802",
    "ach": "0xBc7d6B50616989655AfD682fb42743507003056D",
    "ada": "0x3EE2200Efb3400fAbB9AacF31297cBdD1d435D47",
    "adx": "0x6bfF4Fb161347ad7de4A625AE5aa3A1CA7077819",
    "alice": "0xAC51066d7bEC65Dc4589368da368b212745d63E8",
    "alpa": "0xc5E6689C9c8B02be7C49912Ef19e79cF24977f03",
    "alpaca": "0x8F0528cE5eF7B51152A59745bEfDD91D97091d2F",
    "alpha": "0xa1faa113cbE53436Df28FF0aEe54275c13B40975",
    "ampl": "0xDB021b1B247fe2F1fa57e0A87C748Cc1E321F07F",
    "ankr": "0xf307910A4c7bbc79691fD374889b36d8531B08e3",
    "ankrbnb": "0x52F24a5e03aee338Da5fd9Df68D2b6FAe1178827",
    "antex": "0xCA1aCAB14e85F30996aC83c64fF93Ded7586977C",
    "anymtlx": "0x5921DEE8556c4593EeFCFad3CA5e2f618606483b",
    "aog": "0x40C8225329Bd3e28A043B029E0D07a5344d2C27C",
    "ape": "0xC762043E211571eB34f1ef377e5e8e76914962f9",
    "apx": "0x78F5d389F5CDCcFc41594aBaB4B0Ed02F31398b3",
    "apys": "0x37dfACfaeDA801437Ff648A1559d73f4C40aAcb7",
    "arena": "0xCfFD4D3B517b77BE32C76DA768634dE6C738889B",
    "arpa": "0x6F769E65c14Ebd1f68817F5f1DcDb61Cfa2D6f7e",
    "arv": "0x6679eB24F59dFe111864AEc72B443d1Da666B360",
    "asr": "0x80D5f92C2c8C682070C95495313dDB680B267320",
    "ata": "0xA2120b9e674d3fC3875f415A7DF52e382F141225",
    "atm": "0x25E9d05365c867E59C1904E7463Af9F312296f9E",
    "atom": "0x0Eb3a705fc54725037CC9e008bDede697f62F335",
    "axl": "0x8b1f4432F943c465A973FeDC6d7aa50Fc96f1f65",
    "axs": "0x715D400F88C167884bbCc41C5FeA407ed4D2f8A0",
    "babycake": "0xdB8D30b74bf098aF214e862C90E647bbB1fcC58c",
    "bake": "0xE02dF9e3e622DeBdD69fb838bB799E3F168902c5",
    "balbt": "0x72fAa679E1008Ad8382959FF48E392042A8b06f7",
    "band": "0xAD6cAEb32CD2c308980a548bD0Bc5AA4306c6c18",
    "bat": "0x101d82428437127bF1608F699CD651e6Abf9766E",
    "bath": "0x0bc89aa98Ad94E6798Ec822d0814d934cCD0c0cE",
    "bbt": "0xD48474E7444727bF500a32D5AbE01943f3A59A64",
    "bcfx": "0x045c4324039dA91c52C55DF5D785385Aab073DcF",
    "c98": "0xaEC945e04baF28b135Fa7c640f624f8D90F1C3a6"
}
COIN_SYMBOLS = {
    "0x55d398326f99059ff775485246999027b3197955": "usdt",
    "0x4db5a66e937a9f4473fa95b1caf1d1e1d62e29ea": "weth",
    "0x2170ed0880ac9a755fd29b2688956bd959f933f8": "eth",
    "0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c": "btcb",
    "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d": "usdc",
    "0xe48a3d7d0bc88d552f730b62c006bc925eadb9ee": "fxs",
    "0x949d48eca67b17269629c7194f4b727d4ef9e5d6": "mc",
    "0x90c97f71e18723b0cf0dfa30ee176ab653e89f40": "frax",
    "0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3": "dai",
    "0x4691937a7508860f876c9c0a2a617e7d9e945d4b": "woo",
    "0xbf5140a22578168fd562dccf235e5d43a02ce9b1": "uni",
    "0x51ba0b044d96c3abfca52b64d733603ccc4f0d4d": "super",
    "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c": "wbnb",
    "0xd98438889ae7364c7e2a3540547fad042fb24642": "cell",
    "0x67b725d7e342d7b611fa85e859df9697d9378b2e": "sand",
    "0x2859e4544c4bb03966803b044a93563bd2d0dd4d": "shib",
    '0x8443f091997f06a61670b735ed92734f5628692f': 'bel',
    '0x715d400f88c167884bbcc41c5fea407ed4d2f8a0': 'axs',
    '0xbc7d6b50616989655afd682fb42743507003056d': 'ach',
    "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82": "cake",
    "0xfeea0bdd3d07eb6fe305938878c0cadbfa169042": "8pay",
    "0xfb6115445bff7b52feb98650c87f44907e58f802": "aave",
    "0xbc7d6b50616989655afd682fb42743507003056d": "ach",
    "0x3ee2200efb3400fabb9aacf31297cbdd1d435d47": "ada",
    "0x6bff4fb161347ad7de4a625ae5aa3a1ca7077819": "adx",
    "0xac51066d7bec65dc4589368da368b212745d63e8": "alice",
    "0xc5e6689c9c8b02be7c49912ef19e79cf24977f03": "alpa",
    "0x8f0528ce5ef7b51152a59745befdd91d97091d2f": "alpaca",
    "0xa1faa113cbe53436df28ff0aee54275c13b40975": "alpha",
    "0xdb021b1b247fe2f1fa57e0a87c748cc1e321f07f": "ampl",
    "0xf307910a4c7bbc79691fd374889b36d8531b08e3": "ankr",
    "0x52f24a5e03aee338da5fd9df68d2b6fae1178827": "ankrbnb",
    "0xca1acab14e85f30996ac83c64ff93ded7586977c": "antex",
    "0x5921dee8556c4593eefcfad3ca5e2f618606483b": "anymtlx",
    "0x40c8225329bd3e28a043b029e0d07a5344d2c27c": "aog",
    "0xc762043e211571eb34f1ef377e5e8e76914962f9": "ape",
    "0x78f5d389f5cdccfc41594abab4b0ed02f31398b3": "apx",
    "0x37dfacfaeda801437ff648a1559d73f4c40aacb7": "apys",
    "0xcffd4d3b517b77be32c76da768634de6c738889b": "arena",
    "0x6f769e65c14ebd1f68817f5f1dcdb61cfa2d6f7e": "arpa",
    "0x6679eb24f59dfe111864aec72b443d1da666b360": "arv",
    "0x80d5f92c2c8c682070c95495313ddb680b267320": "asr",
    "0xa2120b9e674d3fc3875f415a7df52e382f141225": "ata",
    "0x25e9d05365c867e59c1904e7463af9f312296f9e": "atm",
    "0x0eb3a705fc54725037cc9e008bdede697f62f335": "atom",
    "0x8b1f4432f943c465a973fedc6d7aa50fc96f1f65": "axl",
    "0x715d400f88c167884bbcc41c5fea407ed4d2f8a0": "axs",
    "0xdb8d30b74bf098af214e862c90e647bbb1fcc58c": "babycake",
    "0xe02df9e3e622debdd69fb838bb799e3f168902c5": "bake",
    "0x72faa679e1008ad8382959ff48e392042a8b06f7": "balbt",
    "0xad6caeb32cd2c308980a548bd0bc5aa4306c6c18": "band",
    "0x101d82428437127bf1608f699cd651e6abf9766e": "bat",
    "0x0bc89aa98ad94e6798ec822d0814d934ccd0c0ce": "bath",
    "0xd48474e7444727bf500a32d5abe01943f3a59a64": "bbt",
    "0x045c4324039da91c52c55df5d785385aab073dcf": "bcfx",
    "0xaec945e04baf28b135fa7c640f624f8d90f1c3a6": "c98"
}
SOLID_COIN = ["weth", "usdt", "usdc", "btcb", "eth"]  # usdt address
# SOLID_COIN = ["usdt", "eth"]  # usdt address
VARIABLE_COIN = [
    'bel',
    'axs',
    'ach',
    'cake', 
    '8pay', 
    'aave', 
    'ach', 
    'ada', 
    'adx', 
    'alice', 
    'alpa', 
    'alpaca', 
    'alpha', 
    'ampl', 
    'ankr', 
    'ankrbnb', 
    'antex', 
    'anymtlx', 
    'aog', 
    'ape', 
    'apx', 
    'apys', 
    'arena', 
    'arpa', 
    'arv', 
    'asr', 
    'ata', 
    'atm', 
    'atom', 
    'axl', 
    'axs', 
    'babycake', 
    'bake', 
    'balbt', 
    'band', 
    'bat', 
    'bath', 
    'bbt', 
    'bcfx', 
    'c98',
    "eth",
    "btcb",
    "usdc",
    "fxs",
    "mc",
    "frax",
    "dai",
    "woo",
    "uni",
    "super",
]



def init_uniswap_router_contract():
    uniswap_router_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
    uniswap_abi_url = "https://api.etherscan.io/api?module=contract&action=getabi&address=" + uniswap_router_address
    response = requests.get(uniswap_abi_url)
    uniswap_abi = response.json()["result"]
    # print("what  is the uniswap abi", uniswap_abi)
    return W3.eth.contract(address=uniswap_router_address, abi=uniswap_abi)


 # def init_pancakeswap_router_contract():




def init_contract(router):
    """Initialize Contract"""
    if router == "pancakeswap_v2":
        with open("panRouterV2Abi.json") as f:
            v2_abi = json.load(f)
        contract_address = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
        return W3.eth.contract(address=contract_address, abi=v2_abi)
    elif router == "uniswap_v2":                      
        with open("UniswapAbi.json") as f:
            v2_abi = json.load(f)
        contract_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
        return W3.eth.contract(address=contract_address, abi=v2_abi)
        # init_uniswap_router_contract()
    # elif roter == ""

        # uniswap_router_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
        # uniswap_abi_url = "https://api.etherscan.io/api?module=contract&action=getabi&address=" + uniswap_router_address
        # response = requests.get(uniswap_abi_url)
        # uniswap_abi = response.json()["result"]
        # print("what is the uniswap abi", uniswap_abi)
        # return W3.eth.contract(address=uniswap_router_address, abi=uniswap_abi)




def get_token_decimal(token):
    with open('ERC20Abi.json') as f:
      erc20_abi = json.load(f)
    token_contract = W3.eth.contract(address=token, abi=erc20_abi)
    decimal = token_contract.functions.decimals().call()
    return decimal



def get_pancake_price_v2(contract, token_a, token_b, amount):
    """Get Pancake Price"""
    try:
      decimal_a = get_token_decimal(token=token_a)
      
      price = contract.functions.getAmountsOut(
          int(amount * 10**decimal_a), [token_a, COINS["wbnb"], token_b]
      ).call()
      decimal_b = get_token_decimal(token=token_b)
      return (price[2] / (10 ** decimal_b), f"{COIN_SYMBOLS[token_a.lower()].upper()}/{COIN_SYMBOLS[token_b.lower()].upper()}")
    except ValueError as e:
      print(f"value error : {e}")
      return (0, 'NULL')
    except Exception as e:
        print(f"and Expected error has occurred {e}")
        return(0,'NULL')
    
def get_uniswap_token_decimal(token):
    with open('UniswapAbi.json') as f:
      erc20_abi = json.load(f)
    token_contract = W3.eth.contract(address=token, abi=erc20_abi)
    decimal = token_contract.functions.decimals().call()
    return decimal      

def get_uniswap_price_v2(contract, token_a,token_b,amount):
    # try:
        with open('uni_routerabi.json') as f:
            router_abi = (json.load(f))['result']
        print(token_a, token_b)
        pair_address = fact_contr.functions.getPair(token_a, token_b).call()
        print(pair_address)

    # except Exception as e:
    #     pass

    #     if not pair_address=="0x0000000000000000000000000000000000000000":
    #
    #         router_contract = W3.eth.contract(address=uniswap_router_address, abi=router_abi)
    #         decimal_a = 18
    #         prices = router_contract.functions.getAmountsOut(int(amount * 10**decimal_a),[token_a,token_b]).call()
    #         decimal_b = 18
    #         return (prices[1] / (10 ** decimal_b), f"{COIN_SYMBOLS[token_a.lower()].upper()}/{COIN_SYMBOLS[token_b.lower()].upper()}")
    #     else:
    #         return (None, None)
    #
    # except Exception as e:
    #     print(f"and Expectedd error has occurred {e}")
    #     return(0,'NULL')
    #
    #

def get_dodo_price(token_a, token_b, amount):
    """Get Dodo Price"""
    try:
      decimal = get_token_decimal(token=token_a)
      # print(int(amount * 10 ** decimal))
      headers = {"User-Agent": "DODO-Example"}
      params = {
          "fromTokenAddress": token_a,
          "fromTokenDecimals": 18,
          "toTokenAddress": token_b,
          "toTokenDecimals": 18,
          "fromAmount": int(amount * 10 ** decimal),
          "slippage": 0.5,
          "userAddr": "0x0000000000000000000000000000000000000000",
          "chainId": 56,
          "rpc": RPC_URL,
          "apikey": DODO_APIKEY,
      }

    #   print("in arametereeeeeeeeeeeeeeeee",params)
      raw_price = requests.get(url=DODO_API_ENDPOINT, headers=headers, params=params).text
      price_data = json.loads(raw_price)
    #   print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",price_data)
    #   routes = json.loads(price_data["data"]["routeData"])["subRoute"][0]["midPath"]
    #   print("pppppppppppppppppppppppppppppppppp",routes)
    #   path = []
    #   for route in routes:
    #       path.append(route["fromToken"])
    #       path.append(route["toToken"])
      path_symbol = [COIN_SYMBOLS[token_a.lower()].upper(), COIN_SYMBOLS[token_b.lower()].upper()]
    #   print("llllllllllllllllllllllllllllllllllllllllll",path_symbol)
      path_symbol_text = "/".join(path_symbol)
      time.sleep(3)
    #   print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",price_data["data"]["resAmount"], path_symbol_text)
      return (price_data["data"]["resAmount"], path_symbol_text)
    except:
      return (0, 'NULL')


def get_price(router, token_a, token_b, contract, amount):
    """Get Price based on Router"""
    if router == "pancakeswap_v2":
        return get_pancake_price_v2(contract, token_a, token_b, amount)
    if router == "dodo_dex":
        return get_dodo_price(token_a, token_b, amount)
    if router == "uniswap_v2":
        return get_uniswap_price_v2(contract,token_a,token_b,amount)

def execute_transaction():
  return None

def execute_query():
    with open("arbitrage_data.csv", "w") as file:
        file.write(
            "DayTime,Arbitrage%,Status,Solid_Coin,Variable_coin,Ex_Name_Buy,Ex_Name_Sell,Buy_pair,Buy_price,Sell_pair,Sell_price"
        )
        print(
            colored(
                "DayTime\t\t\tArbitrage%\t\tStatus\t\tSolid coin\tVariable coin\tEx_Name Buy\tEx_Name Sell\tBuy Routes\tBuy price\t\tSell Routes\tSell price\n",
                "white",
                "on_grey",
                ["bold", "underline"],
            )
        )
        """Main Function to Execute Query and Print Results"""
        # contract = init_contract()

        for sCoin in SOLID_COIN:
            for vCoin in VARIABLE_COIN:
                if sCoin != vCoin:
                    for router_buy in ROUTES:
                        contract = init_contract(router_buy)
                        buy_price, buy_path = get_price(
                            router=router_buy,
                            token_a=COINS[vCoin],
                            token_b=COINS[sCoin],
                            contract=contract,
                            amount=10000

                        )
                        if buy_price is not None:
                            print("Arbitrage buy Price.........0",buy_price,buy_path)
                            for router_sell in ROUTES:
                                if router_buy != router_sell:
                                    contract = init_contract(router_buy),
                                    sell_price, sell_path = get_price(
                                        router=router_sell,
                                        token_a=COINS[sCoin],
                                        token_b=COINS[vCoin],
                                        # contract = init_contract(router)
                                        contract=contract,
                                        amount=buy_price

                                    )
                                    if sell_price is not None:
                                        print("Arbitrage sell Price.........0",sell_price,sell_path)
                                        # print("Available exchanges--------",ccxt.exchanges)
                                        arbitrage = (sell_price - 1) / 1 * 100
                                        status, color = (
                                            ("positive", "green") if arbitrage >0 else ("negative", "red")
                                        )
                                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                        print(
                                            colored(
                                                f"{current_time}\t{arbitrage:.16f}\t{status}\t{sCoin.upper()}\t\t{vCoin.upper()}\t\t{router_buy}\t{router_sell}\t{buy_path}\t{buy_price}\t{sell_path}\t{sell_price}",
                                                color,
                                                "on_grey",
                                                # ["underline"],
                                            )
                                        )
                                        print(colored(f"-" * 200, color))
                                        file.write(
                                            f"\n{current_time},{arbitrage},{status},{sCoin.upper()},{vCoin.upper()},{router_buy},{router_sell},{buy_path},{buy_price},{sell_path},{sell_price}"
                                        )

                                    else:
                                        print(f"Pair doesn't exist ({vCoin, sCoin}) in {router_sell}")
                                        print(f"-" * 200)
                        else:
                            print(f"Pair doesn't exist ({vCoin, sCoin}) in {router_buy}")
                            print(f"-" * 200)

if __name__ == "__main__":
    # get_pancake_price_v2()
    # get_uniswap_price_v2()
    # get_dodo_price()
    execute_query()