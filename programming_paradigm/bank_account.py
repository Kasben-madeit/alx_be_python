class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = float(account_balance) 
        account_balance = 100.00

    def deposit(self,amount):
        self.amount = float(amount)
        self.account_balance += amount

    def withdraw(self,amount):
        self.amount = float(amount)
        self.account_balance -= amount

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    
# d1 = BankAccount(500)
# d1.display_balance()
# d1.deposit(200)
# d1.display_balance()
