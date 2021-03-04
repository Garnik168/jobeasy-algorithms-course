# The greatest common divisor  + Euclidean algorithm

# Find divisor of two or more integers, which are not all zero, is the largest positive integer
# that divides each of the integers.

# What is the greatest common divisor of 54 and 24?
# The number 54 can be expressed as a product of two integers in several different ways:
#
# 54 * 1 = 27 * 2 = 18 * 3 = 9 * 6. Thus the divisors of 54 are: 1, 2, 3, 6, 9, 18, 27, 54.
# Similarly, the divisors of 24 are: 1, 2, 3, 4, 6, 8, 12, 24.
#
# The numbers that these two lists share in common are the common divisors of 54 and 24:
# 1,2,3,6.
#
# The greatest of these is 6. That is, the greatest common divisor of 54 and 24 is 6.

from Algorithms_2.Get_divisors import get_divisors      # this is how to import already created functions
                                                        # from different collections

def in_list(num, list_of_numbers):
    return num in list_of_numbers


def greater_common_divisor(num_1, num_2):
    divisors_num_1 = get_divisors(num_1)
    divisors_num_2 = get_divisors(num_2)

    # print(divisors_num_1)               # Visual purposes
    # print(divisors_num_2)

    result = []
    for number in divisors_num_1:
        if in_list(number, divisors_num_2):
            result.append(number)
    return result[-1]

print(greater_common_divisor(24, 16))
print(greater_common_divisor(24, 48))
print(greater_common_divisor(54, 24))


