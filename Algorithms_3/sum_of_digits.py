def sum_of_digits(num):
    if num > 9:
        return num % 10 + sum_of_digits(num // 10)
    return num

# print(sum_of_digits(123))
# print(sum_of_digits(555))
