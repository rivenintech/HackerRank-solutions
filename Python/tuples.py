# https://www.hackerrank.com/challenges/python-tuples/problem

# -------------------------------------- Task --------------------------------------:
# Given an integer, 'n', and 'n' space-separated integers as input, create a tuple, 't', of those 'n' integers. Then compute and print the result of 'hash(t)'.
# ----------------------------------------------------------------------------------


n = int(input())
t = tuple(map(int, input().split()))
    
print(hash(t))