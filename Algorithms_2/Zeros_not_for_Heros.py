# Zeros not for Heroes
# Numbers ending with zeros are boring. They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway


number = int(input('Enter your, number: '))


def no_zeros_at_the_end(number):
    if number == 0:
        return f"Zero alone is fine, don't worry about it. Poor guy anyway"
    while number % 10 == 0:
        number //= 10
    return number


print(no_zeros_at_the_end(number))

