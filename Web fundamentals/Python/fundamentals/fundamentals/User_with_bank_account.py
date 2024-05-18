class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self

    def display_balance(self):
        return f"Balance: {self.balance}"

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.user_account = {}

    # Deposit method:
    def make_deposit(self, amount=500):
        self.account.deposit(amount)
        return self

# Example usage:
user = User("John Doe", "john@example.com")
user.make_deposit(1000)
print(user.account.display_balance())  # Output: Balance: 1000




    



