#!/usr/bin/python3
# Write a function

# year = 1990
# year = ((10**5)-1) # 99,999
year = 2400
def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
        return leap
    elif year % 100 == 0:
        leap = False
        return leap
    elif year % 4 == 0:
        leap = True
        return leap
    else:
        leap = False
        return leap
    return leap

# year = int(input())
print(is_leap(year))
