class Bank:

    def __init__(self, principal: float, rateOfInterest: float, time: int):
        self.principal = principal
        self.rateOfInterest = rateOfInterest
        self.time = time

class SimpleInterest(Bank):

    def __init__(self, principal: float, rateOfInterest: float, time: int):
        super().__init__(principal, rateOfInterest, time)

    def simpleInt(self):
        return (self.principal * self.rateOfInterest * self.time)/100

class CompoundInterest(Bank):

    def __init__(self, principal: float, rateOfInterest: float, time: int):
        super().__init__(principal, rateOfInterest, time)

    def compoundInt(self):
        totalAmount = self.principal * ((1 + self.rateOfInterest / 100) ** self.time)
        return round(totalAmount - self.principal, 2)

principal = float(input("Enter principal amount : "))
rateOfInterest = float(input("Enter rate Of Interest : "))
time = int(input("Enter time : "))

obj = SimpleInterest(principal, rateOfInterest, time)

print(f"Simple Interest : {obj.simpleInt()}")

obj1 = CompoundInterest(principal, rateOfInterest, time)

print(f"Compound Interest : {obj1.compoundInt()}")
