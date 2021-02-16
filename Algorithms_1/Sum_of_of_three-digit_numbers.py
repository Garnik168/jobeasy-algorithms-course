# Our code generates a random three-digit number and has to sum up all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16.

# n = int(input('Input a number of digits: '))
from random import randint
#
# random_number = randint(100, 999)
# print(f' random number is {random_number}')
#
# def sum_of_three(number):
#     ones = number % 10
#     number = number // 10
#     tens = number % 10
#     hundreds = number // 10
#     return ones + tens + hundreds
#
# print(sum_of_three(random_number))


# Sum of 3 modified
# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0

# This is what I understood you wanted us to do:

n = int(input('Input a number of digits: '))
while n <= 0:
    n = int(input('Input a number of digits(make sure number is > 0, otherwise you will get this prompt again: '))
print(f'User entered {n}, commencing sum of entered digits...')

def sum_n_digits_number(number: int):
    iterable_number = str(number)
    result = 0
    for num in iterable_number:
        result += int(num)
    return result


print(f'Here is the result: {sum_n_digits_number(n)}')


# But I remembered that during the class you wanted us to do something else, here is what I understood:

n = int(input('Input a number for digits: '))
while n <= 0:
    n = int(input('Input a number for digits(make sure number is > 0, otherwise you will get this prompt again: '))
print(f'User want\'s me to create a random number that has "{n}" digits, commencing...')

# range_of_numbers_with_n_digits = range(10**(n - 1), (10**n) - 1) # this for myself, how I got the numbers I need in range

random_number_with_n_digits_to_sum_up = randint(10**(n - 1), (10**n) - 1)
print(f'This is the user\'s randomized number: {random_number_with_n_digits_to_sum_up}\n'
      f'Commencing the sum of randomized number digits...')

def sum_random_n_digit_number(number):
    iterable_number = str(number)
    result = 0
    for num in iterable_number:
        result += int(num)
    return result

print(f'Here is the result: {sum_random_n_digit_number(random_number_with_n_digits_to_sum_up)}')

