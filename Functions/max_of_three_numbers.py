def max_of_two(x,y):
    if x > y:
        return x
    else:
        return y

def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))


# userNum = int(input("Enter "))

print(max_of_three(4,100,-2323))
