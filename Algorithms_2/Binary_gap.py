# Find the maximal sequence of consecutive zeros that surrounded by ones at both ends in the binary representation of a number entered by User.
#
# Examples:
# 9 as a binary number is 1001. The Binary gap is equal to 2 (there are two consecutive zeros in this number).
# 529 as a binary number is 1000010001. The Binary gap is equal to 4.

number = int(input('Please enter a number: '))


def to_bin(number):
    result = ''
    while number > 0:
        result += str(number % 2)
        number //= 2
    return result[::-1]

# print(to_bin(9))
# print(to_bin(529))

# one more wayt o do it using function divmov()
# def to_bin(number):
#     result = ''
#     while number > 0:
#         number, remainder = divmod(number, 2)
#         result += str(remainder)
#     return result[::-1]
# print(to_bin(9))
# print(to_bin(529))

# # there is a function bin() to get binary numbers and oct() to octagonal numbers hex() for hexadecimal
# print(bin(9))
# print(str(bin(9))[2:])
# print(oct(9))
# print(hex(9))


def binary_gap(bin_number):
    print(bin_number)
    max_gap = 0
    counter = 0
    for item in str(bin_number):
        if int(item) == 0:
            counter += 1
        else:
            if counter > 0 and counter > max_gap:
                max_gap = counter
            counter = 0
    return max_gap

print(binary_gap(to_bin(number)))