# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

# -------------------------------------- Task --------------------------------------:
# You are given a string "S".
# Your task is to print all possible size "k" replacement combinations of the string in lexicographic sorted order.
# ----------------------------------------------------------------------------------


from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

# sorting string, so the tuples returned will also be sorted
s = sorted(s)

comb = sorted(list(combinations_with_replacement(s, k)))

for i in comb:
    print("".join(i))