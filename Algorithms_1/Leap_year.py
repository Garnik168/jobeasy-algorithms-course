# When a user enters a year, the code detects if it is a leap year or not.
#
# 1024 - True / False
#
# Any year that is evenly divisible by 4 is a leap year: for example, 1988, 1992, and 1996 are leap years.
# However, there is still a small error that must be accounted for. To eliminate this error, the Gregorian calendar
# stipulates that a year that is evenly divisible by 100 (for example, 1900) is a leap year only if it is also evenly
# divisible by 400.

# divided equally by 4 and 400 == leap year
# divided equally by 4 and not divided by 100 == leap year


year = int(input('Input the year: '))

def leap_year(y):
    # if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:        # My version, to me it is easier to understand this way
    #     return True
    # else:
    #     return False
    if y % 4 != 0:                                    # Ilya's version, also understandable, but reverse logic for me
        return False
    else:
        if y % 100 != 0:
            return True
        else:
            if y % 400 != 0:
                return False
            else:
                return True

print(leap_year(year))
