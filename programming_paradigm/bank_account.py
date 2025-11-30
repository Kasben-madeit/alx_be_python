class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = float(account_balance) 
        self.account_balance = 100.00

    def deposit(self,amount):
        self.amount = float(amount)
        self.account_balance += self.amount
        return True

    def withdraw(self,amount):
        self.amount = float(amount)
        if amount < self.account_balance:
            self.account_balance -= self.amount
            return True
        else:
            return False
       
       

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    
