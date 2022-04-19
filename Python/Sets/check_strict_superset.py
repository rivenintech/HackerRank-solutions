# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# -------------------------------------- Task --------------------------------------:
# You are given a set "A" and "N" other sets. Your job is to find whether set "A" is a strict superset of each of the "N" sets.
# Print "True", if "A" is a strict superset of each of the "N" sets. Otherwise, print "False".
# A strict superset has at least one element that does not exist in its subset.
# ----------------------------------------------------------------------------------


a = set(map(int, input().split()))
n_sets = int(input())

for _ in range(n_sets):
    b = set(map(int, input().split()))
    
    if len(a.intersection(b)) != len(b) or len(a) <= len(b):
        print("False")
        exit()
       
print("True")