# TODO: HW: Rewrite code, which will return only needed element of Fib sequence


n = int(input('Enter needed element of the Fibonacci sequence: '))

def fibonacci(n):
    index = 3
    fib_1 = 1
    fib_2 = 1
    result = [fib_1, fib_2]
    if n == 0:
        return 'Not valid value'
    if n == 1:
        return fib_1          # if you need the element as list just use this instead: return [fib_1]
    if n == 2:
        return fib_2          # if you need the element as list just use this instead: return [fib_2]
    while index <= n:
        result.append(fib_1 + fib_2)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        index += 1
    return result[-1]          # if you need the element as list just use this instead: return [result[-1]]

# print(fibonacci(10))
print(fibonacci(n))