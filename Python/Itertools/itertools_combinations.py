# https://www.hackerrank.com/challenges/itertools-combinations/problem

# -------------------------------------- Task --------------------------------------:
# You are given a string "S". Your task is to print all possible combinations, up to size "k", of the string in lexicographic sorted order.
# ----------------------------------------------------------------------------------


import itertools

s, k = input().split()
k = int(k)

# sorting string, so the tuples returned will also be sorted
s = sorted(s)

for i in range(1, k + 1):
    comb = sorted(list(itertools.combinations(s, i)))
    
    for j in comb:
        print("".join(j))