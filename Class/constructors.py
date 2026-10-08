#Instance Variables
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

s1 = Student("Mohit", "99")

print(s1.name, s1.marks)


#Class Variables

class StudentV:
    schoolName = "ABC School"

    def __init__(self,name):
        self.name = name

s2 = StudentV("Rahul")
s2.name = "mohit"
print(s2.name,s2.schoolName)

s2.age = 24
print(s2.age)

s2.schoolName = "XYZ"
print(s2.schoolName)
