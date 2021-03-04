from Algorithms_3.sum_of_digits import sum_of_digits


def digital_root_recursion(num):
    result = sum_of_digits(num)
    if result > 9:
        return digital_root_recursion(result)
    return result


print(digital_root_recursion(555))
print(digital_root_recursion(123))
print(digital_root_recursion(12))
print(digital_root_recursion(2))
print(digital_root_recursion(0))
print(digital_root_recursion(7))

print('Double Recursion version below:')


def double_rec_root(num):
    if num < 10:
        return num
    if num >= 10:
        result = num % 10 + digital_root_recursion(num // 10)    # now I got it, doesn't matter how you call it
        if result > 9:                                           # as long as you call it it will do what it meant to do
            return digital_root_recursion(result)                # a RECURSION :)
        return result


print(double_rec_root(555))
print(double_rec_root(123))
print(double_rec_root(12))
print(double_rec_root(2))
print(double_rec_root(0))
print(double_rec_root(7))



