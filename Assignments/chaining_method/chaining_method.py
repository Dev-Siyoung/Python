class User:
    def __init__(self):
        self.name = ""
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
       
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
        
    def display_user_balance(self):
        print(self.account_balance)
        return self
        
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
        

first_user = User()
second_user = User()
third_user = User()

first_user.make_deposit(2000).make_deposit(2500).make_deposit(3000).make_withdrawal(5000).display_user_balance()


second_user.make_deposit(1000).make_deposit(1200).make_withdrawal(800).make_withdrawal(500).display_user_balance()


third_user.make_deposit(5000).make_withdrawal(1000).make_withdrawal(500).make_withdrawal(2000).display_user_balance()



first_user.transfer_money(third_user, 1000)
first_user.display_user_balance()
third_user.display_user_balance()
        