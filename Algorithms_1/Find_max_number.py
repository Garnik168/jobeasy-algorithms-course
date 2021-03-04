# Find max number from 3 values, entered manually from a keyboard

value_1 = int(input(f'Enter the first number\'s value here: '))
value_2 = int(input(f'Enter the second number\'s value here: '))
value_3 = int(input(f'Enter the third number\'s value here: '))

def max_number_from_3_values(v1, v2, v3):
    list_of_values = [v1, v2, v3]
    return max(list_of_values)

print(f'The max number that you\'ve intered is: {max_number_from_3_values(value_1, value_2, value_3)}')


def max_of_three(number_1, number_2, number_3):
    max_item = number_1
    if max_item < number_2:
        max_item = number_3
    if max_item < number_3:
        max_item = number_3
    return max_item

print(max_of_three(23, 12, 55))

