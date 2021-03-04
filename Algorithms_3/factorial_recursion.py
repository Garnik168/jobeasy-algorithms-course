def factorial_recursion(number):
    if number < 0:
        return 'No gamma functions please'
    result = 1
    if number == 0:
        return 0
    if number == 1:
        result *= number
        return result
    if number > 1:
        result = number * factorial_recursion(number - 1)
        return result


print(factorial_recursion(2))
print(factorial_recursion(3))
print(factorial_recursion(4))
print(factorial_recursion(5))
print(factorial_recursion(10))
print(factorial_recursion(0))
print(factorial_recursion(1))
print(factorial_recursion(-1))



