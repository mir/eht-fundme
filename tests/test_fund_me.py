from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me
from brownie import accounts, FundMe

def test_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    assert fund_me.addressToAmountFunded(account.address) == 0
