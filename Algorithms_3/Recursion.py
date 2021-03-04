# Recursion - is a method of solving a problem where the solution depends
# on solutions to smaller instances of the same problem.

# reusing Zeros not for Heroes as a recursion

# Zeros not for Heroes
# Numbers ending with zeros are boring. They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

def ZNH_rec(n):                    # in order for recursion to work you need to call the same function into the function
    if n == 0:
        return 0
    if n % 10 == 0:                    # first it will execute 960000 % 10 == 0 and then continue depper into root
        return ZNH_rec(n // 10)        # (960000 // 10 = 96000) to 96000 % 10 == 0, until it reaches 96 % 10 == 6,
    return n                           # at that point it will stop and start returning results to previous functions


print(ZNH_rec(960000))
print(ZNH_rec(1450))
print(ZNH_rec(1050))
print(ZNH_rec(-1050))
