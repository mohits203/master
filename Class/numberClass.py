class Number:

    def __init__(self, num: int):
        self.num = num

    def showNumber(self):
        return self.num

class Operation(Number):

    def __init__(self, num: int):
        super().__init__(num)

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

num = int(input("Enter a number : "))

obj = Operation(num)
print(obj.showNumber())
print(obj.checkEvenOdd())
print(obj.checkNegativePositive())

