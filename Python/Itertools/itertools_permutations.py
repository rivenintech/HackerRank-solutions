# https://www.hackerrank.com/challenges/itertools-permutations/problem

# -------------------------------------- Task --------------------------------------:
# You are given a string "S".
# Your task is to print all possible permutations of size "k" of the string in lexicographic sorted order.
# ----------------------------------------------------------------------------------


import itertools

s, k = input().split()

perm = sorted(list(itertools.permutations(s, int(k))))

for i in perm:
    print("".join(i))