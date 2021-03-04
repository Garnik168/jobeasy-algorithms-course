# Prime number
#
# Check if given number is a prime number
#
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
#
# A Prime number has only two divisors - 1 and itself.
#
# 4: divisors [1, 2, 4] not a Prime number
# 5: divisors [1, 5] a Prime number
# 24: divisors [1, 2, 3, 4, 6, 8, 12, 24] not a Prime number
# 47: divisors [1, 47] a Prime number


def is_prime(given_number):
    if given_number < 2:
        return False
    for number in range(2, given_number):
        if given_number % number == 0:
            return False
    return True


print(is_prime(2))
print(is_prime(7))
print(is_prime(3))
print(is_prime(47))
print(is_prime(9))


# You have a given number. Find all prime numbers before the given number


def prime_numbers(num):
    result = []
    for number in range(2, num):         # range(2, num + 1) if you want to include that number into the list as well
        if is_prime(number):
            result.append(number)
    return result


print(prime_numbers(15))
print(prime_numbers(151))
print(prime_numbers(9))
print(prime_numbers(24))
print(prime_numbers(100))
