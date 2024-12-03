from endpoints import *
from datetime import datetime
import time
from termcolor import colored
from uni_token_analysis import tokens6

SOLID_COIN = [
    # "weth",
    "usdt", "usdc", "btc", "eth"]  # usdt address
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
VARIABLE_COIN2 = [
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
    'eth',
    'btcb',
    'usdc',
    'fxs',
    'mc',
    'frax',
    'dai',
    'woo',
    'uni',
    'super',
    'pol',   # MATIC (Polygon)
    'shib',    # SHIB (Shiba Inu)
    'mkr',     # MKR (Maker)
    'zrx',     # ZRX (0x)
    'sushi',   # SUSHI (SushiSwap)
    'comp',    # COMP (Compound)
    'enj',     # ENJ (Enjin Coin)
    'xrune',    # XRUNE (THORChain)
    'audio',   # AUDIO (Audius)
    'grt',     # GRT (The Graph)
    'crv',     # CRV (Curve DAO Token)
    '1inch',   # 1INCH (1inch)
    'bal',     # BAL (Balancer)
    'ren',     # REN (Ren)
    'lrc',     # LRC (Loopring)
    'omg',     # OMG (OMG Network)
    'knc',     # KNC (Kyber Network)
    'yfii',    # YFII (DFI.Money)
    'bnt',     # BNT (Bancor)
    'lina',    # LINA (Linear)
    'api3',    # API3 (API3)
    'band',    # BAND (Band Protocol)
    'rsr',     # RSR (Reserve Rights)
    'coti',    # COTI (COTI)
    'rlc',     # RLC (iExec RLC)
    'mana',    # MANA (Decentraland)
    'ocean',   # OCEAN (Ocean Protocol)
    'ctsi',    # CTSI (Cartesi)
    'pond',    # POND (Marlin)
    'srm',     # SRM (Serum)
]

tokens5={'BEL': '0xA91ac63D040dEB1b7A5E4d4134aD23eb0ba07e14',
         'AXS': '0xBB0E17EF65F82Ab018d8EDd776e8DD940327B28b',
         'ACH': '0xEd04915c23f00A313a544955524EB7DBD823143d',
         # 'CAKE': '0x152649eA73beAb28c5b49B26eb48f7EAD6d4c898',
         '8PAY': '0x06DDb3a8BC0aBc14f85e974CF1A93a6f8d4909d9',
         'AAVE': '0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9',
         'ALICE': '0xAC51066d7bEC65Dc4589368da368b212745d63E8',
         'ALPHA': '0xa1faa113cbE53436Df28FF0aEe54275c13B40975',
         'AMPL': '0xD46bA6D942050d489DBd938a2C909A5d5039A161', 'ANKR': '0x8290333ceF9e6D528dD5618Fb97a76f268f3EDD4',
         'ALPACA': '0x7cA4408137eb639570F8E647d9bD7B7E8717514A', 'ARPA': '0xBA50933C268F567BDC86E1aC131BE072C6B0b71a',
         'ATA': '0xA2120b9e674d3fC3875f415A7DF52e382F141225', 'AXL': '0x467719aD09025FcC6cF6F8311755809d45a5E5f3',
         'BAT': '0x0D8775F648430679A709E98d2b0Cb6250d2887EF', 'C98': '0xAE12C5930881c53715B369ceC7606B70d8EB229f',
         'ETH': '0x0000000000000000000000000000000000000000', 'BTCB': '0xE57425F1598f9b0d6219706b77f4b3DA573a3695',
         'USDC': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', 'FXS': '0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0',
         'MC': '0xf4eCEd2f682CE333f96f2D8966C613DeD8fC95DD', 'FRAX': '0x853d955aCEf822Db058eb8505911ED77F175b99e',
         'DAI': '0x6B175474E89094C44Da98b954EedeAC495271d0F', 'WOO': '0x4691937a7508860F876c9c0a2a617E7d9E945D4B',
         'UNI': '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984', 'SUPER': '0xe53EC727dbDEB9E2d5456c3be40cFF031AB40A55',
         'WETH': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 'USDT': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
         'RNDR': '0x6De037ef9aD2725EB40118Bb1702EBb27e4Aeb24',
         'BEAM': '0x62D0A8458eD7719FDAF978fe5929C6D342B0bFcE',
         'SAND': '0x3845badAde8e6dFF049820680d1F14bD3903a5d0',
         'NEXO':'0xB62132e35a6c13ee1EE0f84dC5d40bad8d815206',
         'IMX': '0xF57e7e7C23978C3cAEC3C3548E3D615c346e79fF',
         'LPT': '0x58b6A8A3302369DAEc383334672404Ee733aB239',
         'YFI': '0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e',
         'QNT':'0x4a220E6096B25EADb88358cb44068A3248254675',
         'CREAM': '0x2ba592F78dB6436527729929AAf6c908497cB200',
         'GTC': '0xDe30da39c46104798bB5aA3fe8B9e0e1F348163F',
         'LINK': '0x514910771AF9Ca656af840dff83E8264EcF986CA',
         'MLN': '0xec67005c4E498Ec7f55E092bd1d35cbC47C91892'}
path_array=["Bitvavo", "Huobi", "Coinbase", "Bitfinex", "Binance", "Dydx", "Uniswap", "Dodo", "Pancakeswap"]
print(path_array)

exchange_functions = {
    "Bitvavo": get_bitvavo_prices,
    "Huobi": get_huobi_prices,
    "Coinbase": get_coinbase_prices,
    "Bitfinex": get_bitfinex_prices,
    "Binance": get_binance_prices,
    "Dydx": get_dydx_prices,
    "Uniswap": get_uniswap_prices,
    "Dodo": get_dodo_prices,
    "Pancakeswap": get_pancakeswap_prices
}
var_coins3=list(tokens6)

def amount_calculator(usd_price:float):
    if 0<usd_price<=0.1:
        return 1000
    elif 0.1<usd_price<=0.5:
        return 200
    elif 0.5<usd_price<=1:
        return 100
    elif 1<usd_price<=5:
        return 20
    elif 5<usd_price<=10:
        return 10
    elif 10<usd_price<=50:
        return 2
    else:
        return 1

def main():
    print(
        colored(
            "DayTime\t\t\tArbitrage%\t\tStatus\t\tSolid coin\tVariable coin\tEx_Name Buy\tEx_Name Sell\tBuy Routes\tBuy price\t\tSell Routes\tSell price\n",
            "white",
            "on_grey",
            ["bold", "underline"],
        )
    )
    for sCoin in var_coins3:
        for vCoin in var_coins3:
            if sCoin != vCoin:
                # try:
                    prices_dict = {}
                    amount=None
                    for exchange, func in exchange_functions.items():
                        try:
                            if amount==None:
                                amount_in_usd=float(func(vCoin, sCoin, 1)[0])
                                amount=amount_calculator(amount_in_usd)
                            prices_dict[exchange] = func(vCoin, sCoin, amount)[1]
                        except Exception as e:
                            continue
                    if len(prices_dict) > 1:
                        buy_path = path_array[0]
                        sell_path = path_array[0]
                        buy_price = min(prices_dict.values())
                        sell_price = max(prices_dict.values())

                        for ex, price in prices_dict.items():
                            if price == buy_price:
                                buy_path = ex
                            if price == sell_price:
                                sell_path = ex
                        if buy_path != sell_path:
                            # if buy_path=="Uniswap" or sell_path=="Uniswap":
                                print(f"Arbitrage buy Price----> {buy_price} | {vCoin}-{sCoin} | {buy_path} | amount={amount}")
                                print(f"Arbitrage sell Price----> {sell_price} | {vCoin}-{sCoin} | {sell_path} | amount={amount}")

                                profit = (sell_price-buy_price)*amount
                                profit_percentage=((sell_price-buy_price)/buy_price)*100
                                print(f"Investment-----------> {amount_in_usd*amount}")
                                print(f"profit---------------> {profit}  [NOT IN USD]")
                                print(f"profit percentage----> {profit_percentage}")
                                # arbitrage = (sell_price - 1) / 1 * 100

                                if profit_percentage > 1:
                                    status, color = ("positive", "green")
                                elif profit_percentage>0:
                                    status, color = ("positive", "yellow")
                                else:
                                    status, color =("negative", "red")

                                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                print(
                                    colored(
                                        f"{current_time}\t\t{vCoin.upper()}\t\t{sCoin.upper()}\t\t{buy_path}\t\t{sell_path}\t\t{buy_price}\t\t{sell_price}\t\t{status}",
                                        color, force_color=True
                                            # f"{color}",
                                            # ["underline"],
                                        )
                                    )
                                print(colored(f"-" * 200))
                    # file.write(
                    #     f"\n{current_time},{arbitrage},{status},{sCoin.upper()},{vCoin.upper()},{router_buy},{router_sell},{buy_path},{buy_price},{sell_path},{sell_price}"
                    # )
                # except Exception as e:
                #     print(e)

main()