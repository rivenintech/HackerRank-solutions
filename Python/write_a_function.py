# https://www.hackerrank.com/challenges/write-a-function/problem

# -------------------------------------- Task --------------------------------------:
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# In the Gregorian calendar, three conditions are used to identify leap years:
# - The year can be evenly divided by 4, is a leap year, unless:
# - The year can be evenly divided by 100, it is NOT a leap year, unless:
# - The year is also evenly divisible by 400. Then it is a leap year.
# ----------------------------------------------------------------------------------


def is_leap(year):
    leap = False # default value
    
    if year % 4 == 0: # if the year can be evenly divided by 4
        leap = True # it's a leap year, unless:

        if year % 100 == 0: # if the year can be evenly divided by 100
            leap = False # it's NOT a leap year, unless:

            if year % 400 == 0: # if the year is also evenly divisible by 400
                leap = True # it's a leap year

    return leap

year = int(input()) # year to check

print(is_leap(year)) # printing output (True/False)