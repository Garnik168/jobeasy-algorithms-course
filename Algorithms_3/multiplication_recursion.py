def dig_root_rec(number):
    result = 1
    if number == 0:
        return 0
    if abs(number) == 1:
        result *= number
        return result
    if abs(number) > 1:
        result = number * dig_root_rec(abs(number - 1))
        return result


print(dig_root_rec(3))
print(dig_root_rec(5))
print(dig_root_rec(4))