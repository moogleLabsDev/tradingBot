from web3 import Web3, HTTPProvider
import json
import time

PRIVATE_KEY = "bf7b06a4fc15d665ea09ebaf3f9b154c4ff8331cd25b39dd5ee41633e0e2dae3"
RPC_URL = "https://bsc-testnet.publicnode.com"
WBNB = "0xae13d989dac2f0debff460ac112a837c89baa7cd"
BUSD = "0xed24fc36d5ee211ea25a80239fb8c4cfd80f12ee"
USDT="0x55d398326f99059fF775485246999027B3197955"
WETH = "0x4DB5a66E937A9F4473fA95b1cAF1d1E1D62E29EA"
W3 = Web3(HTTPProvider(RPC_URL))
PANCAKE_V2 = "0xde2db97d54a3c3b008a097b2260633e6ca7db1af"
checksum_PANCAKE = W3.to_checksum_address(PANCAKE_V2)

def init_pancake_contract():
    with open("panRouterV2Abi.json") as f:
        v2_abi = json.load(f)
    checksum_address = W3.to_checksum_address(PANCAKE_V2)
    return W3.eth.contract(address=checksum_address, abi=v2_abi)

def init_erc20_contract(address):
    with open("ERC20Abi.json") as f:
        erc20_abi = json.load(f)
    return W3.eth.contract(address=address, abi=erc20_abi)

def swap_pancake():
    contract = init_pancake_contract()
    wallet = W3.eth.account.from_key(PRIVATE_KEY)
    print(wallet.address)
    deadline = round(time.time() + 120)
    USDT="0x55d398326f99059fF775485246999027B3197955"
    # WETH ="0x4DB5a66E937A9F4473fA95b1cAF1d1E1D62E29EA"
    BEL="0x8443f091997f06a61670B735ED92734F5628692F"
    checksum_WBNB = W3.to_checksum_address(USDT)
    checksum_BUSD = W3.to_checksum_address(BEL)
    erc20_contract = init_erc20_contract(checksum_WBNB)
    total_allowance = erc20_contract.functions.allowance(wallet.address, checksum_PANCAKE).call()
    print(total_allowance)
    if(total_allowance < 10000000000000000):
        approve_tx = erc20_contract.functions.approve(checksum_PANCAKE, 99999999999999999999).build_transaction({
            'from': wallet.address,
            'nonce': W3.eth.get_transaction_count(wallet.address),
            'gas': 100000,
            'gasPrice': W3.to_wei('15', 'gwei')
        })
        approved_tx = wallet.sign_transaction(approve_tx)
        W3.eth.send_raw_transaction(approved_tx.rawTransaction)
        print('Token Approved')

    tx_hash = contract.functions.swapExactTokensForTokens(1000000000000000, 1, [checksum_WBNB, checksum_BUSD], wallet.address, deadline).build_transaction({
        'from': wallet.address,
        'nonce': W3.eth.get_transaction_count(wallet.address),
        'gas': 150000,
        'gasPrice': W3.to_wei('20', 'gwei')
    })
    signed_tx = wallet.sign_transaction(tx_hash)
    tx = W3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx)
    print('Token swapped')

swap_pancake()