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
        else:
            print("Insufficient funds")
        return self

    def display_balance(self):
        return f"Balance: {self.balance}"


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  # Dictionary to store multiple accounts

    # Method to add a new account
    def add_account(self, account_name, int_rate=0.02, balance=0):
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self

    # Deposit method
    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
            print(f"Deposited {amount} to {self.name}'s '{account_name}' account")
        else:
            print(f"Account '{account_name}' not found")
        return self

    # Withdrawal method
    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
            print(f"Withdrew {amount} from {self.name}'s '{account_name}' account")
        else:
            print(f"Account '{account_name}' not found")
        return self

    # Display user balance for a specific account
    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            print(f"Name: {self.name}\nEmail: {self.email}\n{self.accounts[account_name].display_balance()}")
        else:
            print(f"Account '{account_name}' not found")
        return self

    # List all accounts
    def list_accounts(self):
        print(f"{self.name}'s accounts:")
        for account_name, account in self.accounts.items():
            print(f"{account_name}: {account.display_balance()}")
        return self

    # Transfer money to another user's account
    def transfer_money(self, amount, other_user, from_account_name, to_account_name):
        if from_account_name in self.accounts and to_account_name in other_user.accounts:
            if self.accounts[from_account_name].balance >= amount:
                self.accounts[from_account_name].withdraw(amount)
                other_user.accounts[to_account_name].deposit(amount)
                print(f"Transferred {amount} from {self.name}'s '{from_account_name}' to {other_user.name}'s '{to_account_name}'")
            else:
                print(f"Insufficient funds in {self.name}'s '{from_account_name}' account")
        else:
            print(f"One or both accounts not found for the transfer")
        return self


# Example usage:
# Creating a user instance
# Creating users
user1 = User("Mourad Thlijeni", "mouradthlijeni@gmail.com")
user2 = User("Wissem", "Wissem69@gmail.com")

# Adding accounts to users
user1.add_account("savings", balance=1000)
user1.add_account("checking", balance=500)
user2.add_account("savings", balance=2000)
user2.add_account("checking", balance=1500)

# Making deposits
user1.make_deposit("savings", 500)
user1.make_deposit("checking", 200)

# Making withdrawals
user1.make_withdrawal("savings", 100)
user1.make_withdrawal("checking", 50)

# Displaying balances
user1.display_user_balance("savings")  # Output: Balance: 1400
user1.display_user_balance("checking")  # Output: Balance: 650

# Listing all accounts for user1
user1.list_accounts()

# Transferring money
user1.transfer_money(200, user2, "savings", "checking")

# Displaying balances after transfer
user1.display_user_balance("savings")  # Output: Balance: 1200
user2.display_user_balance("checking")  # Output: Balance: 1700