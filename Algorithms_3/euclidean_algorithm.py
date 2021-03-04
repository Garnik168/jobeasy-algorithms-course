# Euclide suggested we can find a differences of our numbers until the moment then our numbers become a equal number.
# It will be our greatest common division
#
# 54 & 24
# 1. 54 - 24 = 30  #  now works with 30 and 24
# 2. 30 - 24 = 6 # pair become 24 and 6
# 3. 24 - 6 = 18  # 18 and 6
# 4. 18 - 6 = 12 # 12 and 6
# 5. 12 - 6 = 6 # both numbers are 6 => 6 is the greatest common divisor


def euclid_algorithm(num_1, num_2):
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    return num_1      # or num_2 doesn't matter since they both have to be equal in order to stop while loop


print(euclid_algorithm(54, 24))
print(euclid_algorithm(18, 24))
print(euclid_algorithm(16, 24))
print(euclid_algorithm(454, 2))
