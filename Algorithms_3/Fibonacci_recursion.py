# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1, φ2 = 1,  φn = φn−1 + φn−2.
#
# The task is to display all the numbers from start to n of the Fibonacci sequence φn

# F0 = 0
# F1 = 1
# F2 = 1
# F(n) = F(n-1) + F(n-2)


# Reserved to continue later

# F(0) = 0
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
#
# F(n) = F(n-2) + F(n-1)

def fib_rec(number):
    if number <= 1:
        return number
    else:
        return fib_rec(number - 1) + fib_rec(number - 2)


print(fib_rec(0))
print(fib_rec(1))
print(fib_rec(2))
print(fib_rec(3))
print(fib_rec(4))
print(fib_rec(5))
print(fib_rec(6))
print(fib_rec(7))








