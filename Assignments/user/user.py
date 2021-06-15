class User:
    def __init__(self,name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
       
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        
    def display_user_balance(self):
        print((f"I am {self.name} and my balance is ${self.account_balance}"))
        
    def transfer_money(self,other_user,amount):
        print(f"Transfer success. {self.name} has transfered {amount} to {other_user.name}'s account")
        self.account_balance -= amount
        other_user.account_balance += amount
        

first_user = User("first_user")
second_user = User("second_user")
third_user = User("third_user")

first_user.make_deposit(2000)
first_user.make_deposit(2500)
first_user.make_deposit(3000)
first_user.make_withdrawal(5000)
first_user.display_user_balance()

second_user.make_deposit(1000)
second_user.make_deposit(1200)
second_user.make_withdrawal(800)
second_user.make_withdrawal(500)
second_user.display_user_balance()

third_user.make_deposit(5000)
third_user.make_withdrawal(1000)
third_user.make_withdrawal(500)
third_user.make_withdrawal(2000)
third_user.display_user_balance()

first_user.transfer_money(third_user, 1000)
first_user.display_user_balance()
third_user.display_user_balance()
        