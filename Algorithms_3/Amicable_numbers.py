# Check if two numbers are friendly to each other or not.
#
# Amicable number:
# n1 sum of divisors (except an n1) are equal to n2 and sum of divisors n2 are equal to n1.
# For example: 220 and 284
# 220: divisors [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
# 284: divisors [1, 2, 4, 71, 142]


def get_divisors_excl(number):
    result = []
    for item in range(1, number):
        if number % item == 0:
            result.append(item)
    return result


def sum_numbers_from_list(list_of_numbers):
    result = 0
    for num in list_of_numbers:
        result += num
    return result


def amicable_number(num_1, num_2):
    num_1_list = get_divisors_excl(num_1)
    num_2_list = get_divisors_excl(num_2)
    if sum_numbers_from_list(num_2_list) == num_1 and sum_numbers_from_list(num_1_list) == num_2:
        return f'{num_1} and {num_2} are friendly to each other'
    else:
        return f'{num_1} and {num_2} are not friendly to each other'


print(amicable_number(220, 284))
print(amicable_number(220, 285))

