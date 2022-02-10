import numbers
from tkinter import N

# def add_calc(number1, number2):
#     answer = number1 + number2
#     return answer

# added_number = add_calc(5,5)
# print(added_number + 20)

# ask user how many numbers to add together                         # done
# get input for those numbers                                       # done
# store that number somewhere so that it can be referred back to    # done
# create a for loop? to get the users input
# store those numbers in a list?
# once all numbers have been collected, add them together?

number_arr = []
how_Many_Num = int(input("How many numbers would you like to add together?: "))

#how_Many_Num = int(how_Many_Num)

loop_counter = 0

while how_Many_Num > loop_counter:
    number = int(input("Enter number: "))
    number_arr[loop_counter] = number
    loop_counter += 1

print(numbers)

# number_list = input("Enter number " + i + " :")
# number_list = int(numbers.split(","))

# # for i in range(how_Many_Num, 0, 1):


# # print("outside first for loop")

# for i in number_list:
#     print(number_list[i])


def add_calc(intvar):
    answer = intvar

    return intvar


#   number_list = numbers.split(",")

#     return max(number_list)

# biggest_number = finding_max(input("Enter numbers separated by commas:\n"))    