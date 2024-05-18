class BankAccount:
    # Class attribute to keep track of all instances
    all_accounts = []

    def __init__(self, int_rate=0.0, balance=0.0):
        self.int_rate = int_rate
        self.balance = balance
        # Add each new instance to the list of all accounts
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.all_accounts:
            print("Account Info:")
            account.display_account_info()
            print("#"*20)

# Create two accounts
account1 = BankAccount(int_rate=0.05, balance=0)
account2 = BankAccount(int_rate=0.03, balance=0)

# Perform actions on the first account
account1.deposit(500).deposit(200).deposit(350).withdraw(50).yield_interest().display_account_info()

# Perform actions on the second account
account2.deposit(800).deposit(2000).withdraw(200).withdraw(150).withdraw(50).withdraw(200).yield_interest().display_account_info()

# Print all accounts info using the class method
BankAccount.print_all_accounts_info()
