class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def displayInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name: str, age: int, studentId: str):
        super().__init__(name, age)
        self.studentId = studentId
        
    def displayStudentInfo(self):
        self.displayInfo()
        print(f"Student ID: {self.studentId}")

class GraduateStudent(Student):
    def __init__(self, name: str, age: int, studentId: str, researchTopic: str):
        super().__init__(name, age, studentId)
        self.researchTopic = researchTopic
        
    def displayGraduateInfo(self):
        self.displayStudentInfo()
        print(f"Research Topic: {self.researchTopic}")


name = input("Enter student name : ")
age = int(input("Enter student age : "))
studentId = input("Enter student Id : ")
researchTopic = input("Enter student research topic : ")

obj = GraduateStudent(name, age, studentId, researchTopic)

obj.displayGraduateInfo()
