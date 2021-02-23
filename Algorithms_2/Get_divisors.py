# divisor -  a number (less than a given number) that divides into a given number without a remainder. (remainder of division with them must be equal to 0)
#
# 12 = [1, 12, 2, 6, 3, 4]

def get_divisors(number):
    result = []
    for item in range(1, number):       #(1, number + 1) if you want to include number
        if number % item == 0:
            result.append(item)
    return result

print(get_divisors(12))
print(get_divisors(24))