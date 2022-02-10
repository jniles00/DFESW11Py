def multiply_all_numbers(intvar):
    result = 1
    for i in intvar:
        result *= i

    return result

print(multiply_all_numbers((5,4,3,2,1)))