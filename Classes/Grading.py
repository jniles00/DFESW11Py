student_Name = input("Enter student's name: ")
student_Homework = int(input("Enter homework score: "))
student_Assessment = int(input("Enter assessment score: "))
student_FinalScore = int(input("Enter final score: "))

def gradeCalc(student_Homework, student_Assessment, student_FinalScore):
    final = student_Homework + student_Assessment + student_FinalScore
    final_Percent = (final/175) * 100
    
    return str(final_Percent)

final_ICT = gradeCalc(student_Homework, student_Assessment, student_FinalScore)
print(student_Name + " your final ICT score is: " + final_ICT)