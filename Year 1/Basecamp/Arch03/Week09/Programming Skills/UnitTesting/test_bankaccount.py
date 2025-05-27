from bankaccount import *


def test_sufficient_funds_on_withdraw():
    client = BankAccount("Telmo")
    assert client.deposit(10) == True
    assert client.withdraw(5) == True


def test_insufficient_funds_on_withdraw():
    client = BankAccount("Kacper")
    assert client.withdraw(10) == False


def negative_deposit():
    client = BankAccount("Julian")
    assert client.deposit(-100) == False


def positive_deposit():
    client = BankAccount("Joshua")
    assert client.deposit(999999999999999999) == True
