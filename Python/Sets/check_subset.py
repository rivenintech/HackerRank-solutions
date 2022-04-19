# https://www.hackerrank.com/challenges/py-check-subset/problem

# -------------------------------------- Task --------------------------------------:
# You are given two sets, "A" and "B". Your job is to find whether set "A" is a subset of set "B".

# If set "A" is subset of set "B", print "True".
# If set "A" is not a subset of set "B", print "False".
# ----------------------------------------------------------------------------------


for _ in range(int(input())): # number of test cases
    num_a = int(input())
    a = set(map(int, input().split()))
    num_b = int(input())
    b = set(map(int, input().split()))
    
    if len(a.intersection(b)) == len(a):
        print("True")
    else:
        print("False")