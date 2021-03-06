import pytest
from scripts.fund_and_withdraw import fund_me
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me, LOCAL_BLOCKHAIN_ENVIRONMENTS
from brownie import accounts, network, exceptions


def test_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_only_withdraw():
    if network.show_active() not in LOCAL_BLOCKHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")    
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor })
        