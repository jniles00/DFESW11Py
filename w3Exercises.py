# find out which numbers are divisible by 7 and multiples of 5 between 1500 and 2700

# for i in range(1500, 2700):
#     if i %7 == 0 and i %5 == 0:
#         print(i)

#####################################################################

# convert temperatures to and from celsus, farenheit

# userTemp = input("Enter a temperature number: ")

# userTemp = float(userTemp)

# celsiusVar = userTemp / 5
# print(celsiusVar)

# fahrenheitVar = userTemp - 32/9
# print(fahrenheitVar)

#####################################################################

# counter = 0
# loopCounter = 1

# for loopCounter in range(5):
#     for counter in range(loopCounter):
#         print("*", end="")
#         counter += 1
#     print("")
#     loopCounter += 1

# for loopCounter in range(5,0,-1):
#     for counter in range(loopCounter):
#         print("*", end="")
#         counter += 1
#     print("")
#     loopCounter += 1

##########################################################

# count the number of even and odd numbers from a series of numbers

# numList = (1,2,3,4,5,6,7,8,9)

# evenNum = 0
# oddNum = 0

# for i in numList:
#     if i % 2:
#         evenNum +=1
#     else:
#         oddNum +=1

# print("Even numbers: ", evenNum)
# print("Odd numbers: ", oddNum)

###########################################################

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    print([i])
    print(type[i])
