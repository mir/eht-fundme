from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund_me():
    account = get_account()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    fund_me.fund({"value": entrance_fee, "from": account})

def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": account})

def main():
    fund_me()
    withdraw()