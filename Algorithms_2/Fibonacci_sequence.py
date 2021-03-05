# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1, φ2 = 1,  φn = φn−1 + φn−2.
#
# The task is to display all the numbers from start to n of the Fibonacci sequence φn

# F0 = 0
# F1 = 1
# F2 = 1
# F(n) = F(n-1) + F(n-2)


def fibonacci(n):
    index = 3
    fib_1 = 1
    fib_2 = 1
    result = [fib_1, fib_2]
    if n == 0:
        return 'Not valid value'
    if n == 1:
        return [fib_1]
    if n == 2:
        return result
    while index <= n:
        result.append(fib_1 + fib_2)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        index += 1
    return result


print(fibonacci(10))
print(fibonacci(101))
