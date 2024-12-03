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
RPC_URL = "https://eth-mainnet.g.alchemy.com/v2/UcLnaPDIR4S2rplgaMDMe_g0VmTt4sJ1"
ROUTES = ["pancakeswap_v2","uniswap_v2","dodo_dex"]
# ROUTES = ["uniswap_v2"]
W3 = Web3(HTTPProvider(RPC_URL))



# # Uniswap configuration
# uniswap_router_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
# uniswap_factory_address = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
# uniswap_abi_url = "https://api.etherscan.io/api?module=contract&action=getabi&address=" + uniswap_router_address
# response = requests.get(uniswap_abi_url)
# uniswap_abi = response.json()["result"]



with open("panRouterV2Abi.json") as f:
    router_v2_abi = (json.load(f))
router_contract_address = "0xEfF92A263d31888d860bD50809A8D171709b7b1c"
router_contract=W3.eth.contract(address=router_contract_address, abi=router_v2_abi)


with open("pancakefactory.json") as f:
    factory_v2_abi = (json.load(f))['result']
factory_contract_address = "0x1097053Fd2ea711dad45caCcc45EfF7548fCB362"
factory_contract=W3.eth.contract(address=factory_contract_address, abi=factory_v2_abi)

decimal_dict={'0xA91ac63D040dEB1b7A5E4d4134aD23eb0ba07e14': 18, '0xBB0E17EF65F82Ab018d8EDd776e8DD940327B28b': 18, '0xEd04915c23f00A313a544955524EB7DBD823143d': 8, '0x06DDb3a8BC0aBc14f85e974CF1A93a6f8d4909d9': 18, '0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9': 18, '0xAC51066d7bEC65Dc4589368da368b212745d63E8': 6, '0xa1faa113cbE53436Df28FF0aEe54275c13B40975': 18, '0xD46bA6D942050d489DBd938a2C909A5d5039A161': 9, '0x8290333ceF9e6D528dD5618Fb97a76f268f3EDD4': 18, '0x7cA4408137eb639570F8E647d9bD7B7E8717514A': 18, '0xBA50933C268F567BDC86E1aC131BE072C6B0b71a': 18, '0xA2120b9e674d3fC3875f415A7DF52e382F141225': 18, '0x467719aD09025FcC6cF6F8311755809d45a5E5f3': 6, '0x0D8775F648430679A709E98d2b0Cb6250d2887EF': 18, '0xAE12C5930881c53715B369ceC7606B70d8EB229f': 18, '0xE57425F1598f9b0d6219706b77f4b3DA573a3695': 18, '0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0': 18, '0xf4eCEd2f682CE333f96f2D8966C613DeD8fC95DD': 2, '0x853d955aCEf822Db058eb8505911ED77F175b99e': 18, '0x6B175474E89094C44Da98b954EedeAC495271d0F': 18, '0x4691937a7508860F876c9c0a2a617E7d9E945D4B': 18, '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984': 18, '0xe53EC727dbDEB9E2d5456c3be40cFF031AB40A55': 18, '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': 18, '0xdAC17F958D2ee523a2206206994597C13D831ec7': 6, '0x6De037ef9aD2725EB40118Bb1702EBb27e4Aeb24': 18, '0x62D0A8458eD7719FDAF978fe5929C6D342B0bFcE': 18, '0x3845badAde8e6dFF049820680d1F14bD3903a5d0': 18, '0xB62132e35a6c13ee1EE0f84dC5d40bad8d815206': 18, '0xF57e7e7C23978C3cAEC3C3548E3D615c346e79fF': 18, '0x58b6A8A3302369DAEc383334672404Ee733aB239': 18, '0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e': 18, '0x4a220E6096B25EADb88358cb44068A3248254675': 18, '0x2ba592F78dB6436527729929AAf6c908497cB200': 18, '0xDe30da39c46104798bB5aA3fe8B9e0e1F348163F': 18, '0x514910771AF9Ca656af840dff83E8264EcF986CA': 18, '0xec67005c4E498Ec7f55E092bd1d35cbC47C91892': 18, '0x455e53CBB86018Ac2B8092FdCd39d8444aFFC3F6': 18, '0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE': 18, '0x69fa0feE221AD11012BAb0FdB45d444D3D2Ce71c': 18, '0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C': 18, '0xBA11D00c5f74255f56a5E366F4F77f5A186d7f55': 18, '0x320623b8E4fF03373931769A31Fc52A4E78B5d70': 18, '0x607F4C5BB672230e8672085532f7e901544a7375': 9, '0x967da4048cD07aB37855c090aAF366e4ce1b9F48': 18}
def get_pancake_price_v2(token_a, token_b, amount=1):
    """Get Pancake Price"""
    # try:
    decimal_a = decimal_dict[token_a]

    price = router_contract.functions.getAmountsOut(amount*int(10 ** decimal_a), [token_a, token_b]).call()
    decimal_b = decimal_dict[token_b]
    return (price[1] / (10 ** decimal_b))

    # except Exception as e:
    #     return (0)


print(get_pancake_price_v2('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', '0xdAC17F958D2ee523a2206206994597C13D831ec7', 1))


