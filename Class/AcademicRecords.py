class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print(f"{self.name} have {self.age} years old.")

class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def addGrade(self, grade):
        self.grade = grade

    def displayGrades(self):
        return self.grade

name = input("Enter the name : ")
age = input("Enter the age : ")
grades = input("Enter the grades list. ex : [\"B\", \"A+\", \"A++\"] : ")
obj = Student(name,age)
obj.displayInfo()

obj.addGrade(grades)
print(obj.displayGrades())
