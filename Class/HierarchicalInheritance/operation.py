class Operation:

    def read(self):
        self.a = int(input("Enter the first value : "))
        self.b = int(input("Enter the first value : "))

    def show(self):
        print(f"The values are: a = {self.a}, b = {self.b}")
        return [self.a, self.b]

    def add(self):
        sumOfTwo = self.a + self.b
        return sumOfTwo

obj = Operation()
obj.read()
show = obj.show()
print(show)
sumOfTwo = obj.add()
print(f"sum : {sumOfTwo}")


class Result:

    def setDetails(self):
        self.m1 = int(input("Enter the m1 value : "))
        self.m2 = int(input("Enter the m2 value : "))
        self.m3 = int(input("Enter the m3 value : "))
        self.rollNum = int(input("Enter the Roll Number : "))

    def calper(self):
        per = (self.m1+self.m2+self.m3)*100/300
        result = f"{self.rollNum} have {per}%"
        return result


obj1 = Result()
obj1.setDetails()
calPer = obj1.calper()
print(calPer)

class Number:

    def read(self):
        self.num = int(input("Enter a number : "))

    def showNumber(self):
        return self.num

    def sumOfNumbers(self):
        num = self.num
        total = 0

        while num > 0:
            n = num % 10
            total = total + n
            num = num // 10

        return total

obj3 = Number()
obj3.read()
showNumber = obj3.showNumber()
print(showNumber)

sumOfNumbers = obj3.sumOfNumbers()
print(sumOfNumbers)
