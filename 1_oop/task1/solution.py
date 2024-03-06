import logging

# Настройка логирования
logging.basicConfig(filename='bank_account.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class BankAccount:
    def __init__(self, first_name, last_name, account_number, balance, currency):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def deposit(self, amount) -> int:
        if amount > 0:
            self.balance += amount
            logging.info(f"Депозит в размере {amount} {self.currency} выполнен успешно. Новый баланс: {self.balance} {self.currency}")
            return self.balance
        else:
            logging.error("Сумма депозита должна быть положительной.")
            return self.balance

    def withdraw(self, amount) -> int:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            logging.info(f"Снятие в размере {amount} {self.currency} выполнено успешно. Новый баланс: {self.balance} {self.currency}")
            return self.balance
        elif amount > self.balance:
            logging.error("Недостаточно средств на счете.")
            return self.balance
        else:
            logging.error("Сумма снятия должна быть положительной.")
            return self.balance

    def get_balance(self) -> int:
        logging.info(f"Текущий баланс: {self.balance} {self.currency}")
        return self.balance

    def get_account_info(self):
        account_info = f"Имя: {self.first_name} {self.last_name}, Номер счета: {self.account_number}, Баланс: {self.balance} {self.currency}"
        logging.info(account_info)
        return account_info

# Пример использования класса BankAccount
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
