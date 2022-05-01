# https://www.hackerrank.com/challenges/itertools-product/problem

# -------------------------------------- Task --------------------------------------:
# You are given a two lists "A" and "B". Your task is to compute their cartesian product "A" x "B".

# Example:
# A = [1, 2]
# B = [3, 4]
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
# ----------------------------------------------------------------------------------


import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

product = list(itertools.product(A, B))

print(*product)