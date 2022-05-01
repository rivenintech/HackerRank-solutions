# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

# -------------------------------------- Task --------------------------------------:
# You are given a list of "N" lowercase English letters.
# For a given integer "K", you can select any "K" indices (assume 1-based indexing) with a uniform probability from the list.
# Find the probability that at least one of the "K" indices selected will contain the letter: 'a'.

# Output a single line consisting of the probability that at least one of the "K" indices selected contains the letter: 'a'.
# ----------------------------------------------------------------------------------


from itertools import combinations

length = int(input())
ls = list(input().split())
k = int(input())

count = 0

# create all possible combinations
comb = list(combinations(ls, k))

# count how many combinations contain 'a'
for i in comb:
    if 'a' in i:
        count += 1

print(count / len(comb))