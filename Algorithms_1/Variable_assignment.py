# User inputs two numbers. One number is assigned to a variable, the other number is assigned to b variable.
# The task is to invert the variables, so that the first variable contains the second number, while the first number
# is in the second variable.

a = int(input('Input value a: '))
b = int(input('Input value b: '))

print(f'a = {a}, b = {b}')

# First version
# temp = a
# a = b
# b = temp
#
# print(f'a = {a}, b = {b}')

# # Second version ( a = 10, b = 5 exp)
# a = a + b          # 10 + 5 = 15
# b = a - b          # 15 - 5 = 10
# a = a - b          # 15 - 10 = 5
#
# print(f'a = {a}, b = {b}')

# Third version POWER OF PYTHON
a, b = b, a

print(f'a = {a}, b = {b}')


