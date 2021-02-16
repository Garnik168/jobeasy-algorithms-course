# Count odd and even digits of the whole number.
# E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)
# and  2 odd digits (3 and 5).

number = int(input('Enter the number: '))

print(f"You've entered: {number}, commencing count of even and odd digits in the number...")

def count_odd_and_even_digits(number):
    even_count = 0
    odd_count = 0
    for num in str(abs(number)):
        if int(num)% 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return f'In this number {even_count} is/are even and {odd_count} is/are odd'

print(count_odd_and_even_digits(number))



