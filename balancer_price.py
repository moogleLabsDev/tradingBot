from web3 import Web3
import json
from uni_token_analysis import tokens6

# Connect to an Ethereum node
RPC = "https://eth-mainnet.g.alchemy.com/v2/UcLnaPDIR4S2rplgaMDMe_g0VmTt4sJ1"
web3 = Web3(Web3.HTTPProvider(RPC))

# Check if connected
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum node")

# Balancer Pool ABI (simplified for this example)
BALANCER_POOL_ABI = json.loads("""
[
    {
        "constant": true,
        "inputs": [{"internalType": "address", "name": "token", "type": "address"}],
        "name": "getBalance",
        "outputs": [{"internalType": "uint256", "name": "balance", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [{"internalType": "address", "name": "token", "type": "address"}],
        "name": "getDenormalizedWeight",
        "outputs": [{"internalType": "uint256", "name": "weight", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
""")

# Balancer pool and token addresses
BALANCER_POOL_ADDRESS = "0xYourBalancerPoolAddress"
TOKEN_A_ADDRESS = "0xYourTokenAAddress"
TOKEN_B_ADDRESS = "0xYourTokenBAddress"

# Create contract instance
balancer_pool = web3.eth.contract(address=BALANCER_POOL_ADDRESS, abi=BALANCER_POOL_ABI)

# Fetch token balances and weights
def fetch_balance_and_weight(token):
    try:
        balance = balancer_pool.functions.getBalance(token).call()
        weight = balancer_pool.functions.getDenormalizedWeight(token).call()
        return balance, weight
    except Exception as e:
        print(f"Error fetching balance and weight: {e}")
        return None, None

# Calculate spot price
def calculate_spot_price(balance_a, weight_a, balance_b, weight_b):
    spot_price = (balance_b / weight_b) / (balance_a / weight_a)
    return spot_price

# Fetch balances and weights
balance_a, weight_a = fetch_balance_and_weight(TOKEN_A_ADDRESS)
balance_b, weight_b = fetch_balance_and_weight(TOKEN_B_ADDRESS)

if balance_a and weight_a and balance_b and weight_b:
    # Calculate spot prices
    spot_price_a_to_b = calculate_spot_price(balance_a, weight_a, balance_b, weight_b)
    spot_price_b_to_a = calculate_spot_price(balance_b, weight_b, balance_a, weight_a)

    print(f"Token A to Token B spot price: {spot_price_a_to_b}")
    print(f"Token B to Token A spot price: {spot_price_b_to_a}")
else:
    print("Failed to fetch balances or weights.")
