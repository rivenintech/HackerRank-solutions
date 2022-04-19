# https://www.hackerrank.com/challenges/symmetric-difference/problem

# -------------------------------------- Task --------------------------------------:
# Given "2" sets of integers, "M" and "N", print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either "M" or "N" but do not exist in both.
# ----------------------------------------------------------------------------------


M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

ls = list(a.difference(b)) + list(b.difference(a))
ls.sort()

for x in ls:
    print(x)