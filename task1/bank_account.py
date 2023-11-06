from ast import main
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class BankAccount:
    def __init__(self, first_name: str, last_name: str, account_numbe: str, balance: int, currency: str):
        raise Exception('Implement me')

    def deposit(self, amount) -> int:
        raise Exception('Implement me')

    def withdraw(self, amount) -> int:
        raise Exception('Implement me')

    def get_balance(self) -> int:
        raise Exception('Implement me')

    def get_account_info(self) -> str:
        raise Exception('Implement me')


# Пример использования класса BankAccount
if __name__ == '__main__':
    account1 = BankAccount("Иван", "Иванов", "12345", 1000, "RUB")
    account2 = BankAccount("Петр", "Петров", "67890", 500, "USD")

    print(account1.get_account_info())
    account1.deposit(500)
    account1.withdraw(200)
    account1.get_balance()

    print(account2.get_account_info())
    account2.deposit(300)
    account2.withdraw(700)
    account2.get_balance()
