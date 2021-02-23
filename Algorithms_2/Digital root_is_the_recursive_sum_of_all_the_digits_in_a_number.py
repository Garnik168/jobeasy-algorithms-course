# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


number = int(input('Enter the number: '))

def digital_root(number):
    while number >= 10:
        number = sum([int(n) for n in str(number)])
    return number

print(digital_root(number))

# Ilya I got the solution above, but I've spent over 3 hours trying to figure out how to do it without function sum()
# Please look a the code below, I really want to understand, why I'm getting infinite loop, there are several ways of
# doing it, but let's think that i want to go with the most simple one, at least for me it's the most simple one:

# def digital_root(number):
#     result = 0
#     while len(str(number)) > 1:
#         for digit in str(number):
#             result += int(digit)
#         number = result               # Here is the problem, even PyCharm is highlighting it, but I can't figure it out
#     return number                   # Please explain, I guess I don't know enough of the while loops
#                                  # Shouldn't number be reassigned and then go through the loop again? what I'm missing?