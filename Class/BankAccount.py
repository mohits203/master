class BankAccount:
    
    def __init__(self, accountHolder: str, balance: float):
        self.accountHolder = accountHolder
        self.balance = balance

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

    def __init__(self, accountHolder: str, balance: float, interestRate: float):
        super().__init__(accountHolder, balance)
        self.interestRate = interestRate

    
    def calculateInterest(self):
        interest = self.balance * self.interestRate/100
        return interest

accountHolder = input("Name of the account holder : ")
balance = float(input("Current balance in the account : "))
interestRate = float(input("The interest rate for the savings account : "))

obj = SavingsAccount(accountHolder, balance, interestRate)
afterDeposit = obj.deposit(2000)
afterWithdraw = obj.withdraw(500)
displayBal = obj.displayBalance()
calInterest = obj.calculateInterest()
print(f"after Deposit : {afterDeposit}")
print(f"after Withdraw : {afterWithdraw}")
print(f"Total Balance : {displayBal}")
print(f"Total interest : {calInterest}")
