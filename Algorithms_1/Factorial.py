# When user enters a number, it's Factorials is displayed

n = int(input('Input a number: '))

def factorial(number):
    if number < 0:
        return "I don't like Gamma Function"
    if number == 0:
        return 1
    result = 1
    for item in range(1, number + 1):
        result *= item
    return result

print(factorial(n))


# You can also use math.factorial FUNCTION if you import math
#
# import math
#
# n = int(input('Input a number: '))
#
# def factorial(number):
#     return math.factorial(number)
#
# print(factorial(n))

