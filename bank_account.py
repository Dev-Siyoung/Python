class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(self.balance)
        return self
    
    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        return self


first_account = BankAccount(0.02, 5000)
second_account = BankAccount(0.025, 10000)

first_account.deposit(3000).deposit(6000).deposit(6000).withdraw(4000).yield_interest().display_account_info()
second_account.deposit(5000).deposit(6000).withdraw(2000).withdraw(1000).withdraw(500).withdraw(2000).yield_interest().display_account_info()