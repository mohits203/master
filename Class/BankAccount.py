class BankAccount:
    
    def __init__(self):
        self.accountHolder = input("Name of the account holder : ")
        self.balance = float(input("Current balance in the account : "))

    def deposit(self, amount):
        try:
            self.balance = self.balance + amount
            return self.balance
        except ValueError:
            e = "That is not a valid number. Please try again."
        return e

    def withdraw(self, amount):
        try:
            self.balance = self.balance - amount
            return self.balance
        except ValueError:
            e = "That is not a valid number. Please try again."
            return e

    def displayBalance(self):
        return self.balance

class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__()
        self.interestRate = float(input("The interest rate for the savings account : "))

    
    def calculateInterest(self):
        interest = self.balance * self.interestRate/100
        return interest


obj = SavingsAccount()
afterDeposit = obj.deposit(2000)
afterWithdraw = obj.withdraw(500)
displayBal = obj.displayBalance()
calInterest = obj.calculateInterest()
print(f"after Deposit : {afterDeposit}")
print(f"after Withdraw : {afterWithdraw}")
print(f"Total Balance : {displayBal}")
print(f"Total interest : {calInterest}")
