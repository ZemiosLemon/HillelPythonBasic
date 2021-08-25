import datetime
from uuid import uuid4


class BankAccount:

    def __init__(self, account_name: str, balance: float):
        self.account_name = account_name
        self.uuid = uuid4()
        self.transactions = []
        self.balance = balance
        self.commission = 0.01

    def deposit(self, currency: float):
        self.balance += currency - currency * self.commission
        self.transactions.append(['deposit', self.balance, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

    def withdrawal(self, currency: float):
        self.balance -= currency + currency * self.commission
        self.transactions.append(['withdrawal', self.balance, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

    def get_balance(self):
        return self.balance


account_client = BankAccount('Bank ID', 2354)
account_client.deposit(5500)
account_client.withdrawal(2000)
print(account_client.transactions)
print(account_client.get_balance())