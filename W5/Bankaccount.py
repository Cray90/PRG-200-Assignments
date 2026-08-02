
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited into account {self.account_number}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from account {self.account_number}")

    def get_balance(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")
        print("-" * 30)


accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

bank_accounts = {}

for name, account_number, balance in accounts:
    bank_accounts[account_number] = BankAccount(name, account_number, balance)

bank_accounts["A002"].deposit(3000)
bank_accounts["A003"].withdraw(15000)   # Should fail
bank_accounts["A001"].withdraw(2000)

print("\nFinal Account Balances")
print("=" * 30)

for account in bank_accounts.values():
    account.get_balance()