from brownie import FundMe, MockV3Aggregator, config, accounts, network
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKHAIN_ENVIRONMENTS)

def main():
    deploy_fund_me()

def deploy_fund_me():
    account = get_account()
    print(f"Active network is {network.show_active()}")
    if network.show_active() not in LOCAL_BLOCKHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1]  

    fund_me = FundMe.deploy(
        price_feed_address, # price feed address
        {"from": account},
         publish_source=config["networks"][network.show_active()].get("verify")
        )
    print(f"Contract is deployed to {fund_me.address}")
