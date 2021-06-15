
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
    



class User:
    def __init__(self, name):
        self.name = "SiYoung"
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
       
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
        
    def display_user_balance(self):
        print(f"My name is {self.name} and I have ${self.account.balance}")
        return self




SiYoung = User("SiYoung")
SiYoung.make_deposit(1000)
SiYoung.make_withdrawal(500)
SiYoung.display_user_balance()




