# function to work out grade based on marks
# should take input for student name, homework score /25, assessment score /50 and final exam score /100
# should output their name and final ICT grade as a percentage
# inputs and prints should not be inside functions
# stretch goal: include grade boundaries that the program ouputs a grade for (A,B,C,etc)

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

# final_Grade = print("Student's final grade was: ", final_Percent)