# Let’s use division instead of subtraction. New value will be remainder of division.
# If remainder is 0 - we have our greatest common divisor
#
# 54 & 24
# 1. 54 % 24 = 6  #  now works with 6 and 24
# 2. 24 % 6 = 0 # pair become 24 and 6
#
# That’s it :)


def euclid_algorithm_pro(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2     # same as num_1 = num_1 % num_2
        else:
            num_2 %= num_1
    return num_1 + num_2       # since while loop will stop right after any of the numbers == 0
                               # and at this point one of them will be == 0


print(euclid_algorithm_pro(54, 24))
print(euclid_algorithm_pro(48, 24))
print(euclid_algorithm_pro(16, 24))
print(euclid_algorithm_pro(16, 17))
