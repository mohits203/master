class Student:

    def __init__(self, name: str, rollNumber: int, studentClass: str):
        self.name = name
        self.rollNumber = rollNumber
        self.studentClass = studentClass

    def show(self):
        print(f"{self.name} have in class {self.studentClass} and his/her roll number is {self.rollNumber}")

class Marks:

    def __init__(self, math: int, science: int, english: int):
        self.math = math
        self.science = science
        self.english = english

    def marksCal(self):
        return self.math + self.science + self.english

    def percentage(self):
        return (self.math + self.science + self.english)*100/300

class Sports(Student, Marks):

    def __init__(self, name: str, rollNumber: int, studentClass: str, math: int, science: int, english: int, sportsName: str, sportsGrade: str):
        Student.__init__(self, name, rollNumber, studentClass)
        Marks.__init__(self, math, science, english)
        self.sportsName = sportsName
        self.sportsGrade = sportsGrade

    def studentDetails(self):
        self.show()
        print(f"Total Marks : {self.marksCal()}")
        print(f"Marks percentage : {self.percentage()}")

    def sportsDetail(self):
        print(f"{self.name} have {self.sportsGrade} grade in {self.sportsName} sport")

name = input("Enter the student name : ")
rollNumber = int(input("Enter the student's roll number : "))
studentClass = input("Enter the student's class : ")

math = int(input("Enter the Marks in Mathematics : "))
science = int(input("Enter the Marks in Science : "))
english = int(input("Enter the Marks in English : "))

sportsName = input("Enter the sports name : ")
sportsGrade = input("Enter the sports grade : ")

obj = Sports(name, rollNumber, studentClass, math, science, english, sportsName, sportsGrade)
obj.studentDetails()
obj.sportsDetail()
