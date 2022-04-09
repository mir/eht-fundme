from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2000e8
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-forked", "mainnet-fork-dev"]
LOCAL_BLOCKHAIN_ENVIRONMENTS = ["development","ganache-local"]

def get_account():
    if (network.show_active() in LOCAL_BLOCKHAIN_ENVIRONMENTS 
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"Active network is {network.show_active}")
    print("Deploying mocks...")
    if (len(MockV3Aggregator) <= 0):
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMALS, # Decimals
            Web3.toWei(STARTING_PRICE, "ether"), # Cost (wei)
            {"from": get_account()})
        print("MockV3Aggregator is deployed")