from brownie import accounts, FundMe
from scripts.helper import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    print(f"Using account {account}")
    minimum_amount = fund_me.getEntranceFee()
    print(f"Entrance fee is {minimum_amount}")
    print(f"Current price {fund_me.getPrice()}")
    fund_me.fund({"from": account, "value": minimum_amount})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print(f"Using account {account}")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
