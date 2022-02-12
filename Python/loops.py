# https://www.hackerrank.com/challenges/python-loops/problem

# -------------------------------------- Task --------------------------------------:
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i^2. Constraints: 1 <= n <= 20
# ----------------------------------------------------------------------------------


n = int(input())

# printing all numbers with power of 2
for i in range(n):
    print(i**2)