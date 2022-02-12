# https://www.hackerrank.com/challenges/python-print/problem

# -------------------------------------- Task --------------------------------------:
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between.
# ----------------------------------------------------------------------------------


n = int(input())

# creating range 1 - n and printing numbers in loop (without new line) 
for x in range(1, n + 1):
    print(x, end='')