from unicodedata import name

# def printFunction():
#     print("This is a print function")

# count = 0
# while(count < 5):
#     printFunction()
#     print("it has run :", count)
#     count += 1



def printedFunction(inputvar):
    printVar = name + " has printed a function!"
    return printVar

name = "Jimothy"
print(printedFunction(name))
name = "Johnold"
print(printedFunction(name))
name = "Alex"
print(printedFunction(name))