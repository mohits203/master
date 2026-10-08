class Student:

    def __init__(self):
        self.name = input("Enter the student name : ")
        self.rollNumber = int(input("Enter the student's roll number : "))
        self.studentClass = input("Enter the student's class : ")

    def show(self):
        print(f"{self.name} have in class {self.studentClass} and his/her roll number is {self.rollNumber}")

class Marks:

    def __init__(self):
        self.math = int(input("Enter the Marks in Mathematics : "))
        self.science = int(input("Enter the Marks in Science : "))
        self.english = int(input("Enter the Marks in English : "))

    def marksCal(self):
        return self.math + self.science + self.english

    def percentage(self):
        return (self.math + self.science + self.english)*100/300

class Sports(Student, Marks):

    def __init__(self):
        Student.__init__(self)
        Marks.__init__(self)
        self.sportsName = input("Enter the sports name : ")
        self.sportsGrade = input("Enter the sports grade : ")

    def sportsDetail(self):
        print(f"{self.name} have {self.sportsGrade} grade in {self.sportsName} sport")

obj = Sports()
obj.show()
marks = obj.marksCal()
print(f"Total marks : {marks}")
percentage = obj.percentage()
print(f"Total percentage : {percentage}")
obj.sportsDetail()
