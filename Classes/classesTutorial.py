from GradeFunction import gradeCalc
import Grading

class Student:
    def __init__(self, name, age, studentClass):
        self.name = name
        self.age = age
        self.studentClass = studentClass


John = Student("John", "21", "Class_2")
Jane = Student("Jane", "22", "Class_4")

print(getattr(John, "age"))