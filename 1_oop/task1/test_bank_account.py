import pytest
from bank_account import BankAccount


# Фикстура для создания экземпляра класса BankAccount для каждого теста
@pytest.fixture
def bank_account():
    return BankAccount("Иван", "Иванов", "12345", 1000, "RUB")


def test_deposit(bank_account):
    initial_balance = bank_account.balance
    deposited_amount = 500
    new_balance = bank_account.deposit(deposited_amount)
    assert new_balance == initial_balance + deposited_amount


def test_withdraw(bank_account):
    initial_balance = bank_account.balance
    withdrawn_amount = 200
    new_balance = bank_account.withdraw(withdrawn_amount)
    assert new_balance == initial_balance - withdrawn_amount


def test_withdraw_insufficient_funds(bank_account):
    withdrawn_amount = 2000
    new_balance = bank_account.withdraw(withdrawn_amount)
    assert new_balance == bank_account.balance  # Баланс не должен измениться


def test_get_balance(bank_account):
    balance = bank_account.get_balance()
    assert balance == bank_account.balance


def test_negative_withdraw(bank_account):
    balance = bank_account.get_balance()
    new_balance = bank_account.withdraw(-100)
    assert new_balance == balance
