class Number:

    def __init__(self):
        self.num = int(input("Enter a number : "))

    def showNumber(self):
        return self.num

class Operation(Number):

    def checkEvenOdd(self):
        if self.num%2 == 0:
            result = "Even"
        else:
            result = "Odd"
        return result

    def checkNegativePositive(self):
        if self.num >= 0:
            result = "Positive"
        else:
            result = "Negative"
        return result

obj = Operation()
print(obj.showNumber())
print(obj.checkEvenOdd())
print(obj.checkNegativePositive())

