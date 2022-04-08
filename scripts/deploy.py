from brownie import FundMe, MockV3Aggregator, config, accounts, network
from scripts.helpful_scripts import get_account



def main():
    deploy_fund_me()


def deploy_fund_me():
    account = get_account()
    print(f"Active network is {network.show_active()}")
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"Active network is {network.show_active}")
        print("Deploying mocks...")
        mock_aggregator = MockV3Aggregator.deploy(18,2000e18,{"from": account})
        print("Mocks deployed")
        price_feed_address = mock_aggregator.address

    fund_me = FundMe.deploy(
        price_feed_address, # price feed address
        {"from": account},
         publish_source=config["networks"][network.show_active()]["verify"]
        )
    print(f"Contract is deployed to {fund_me.address}")
