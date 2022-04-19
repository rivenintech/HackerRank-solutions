# https://www.hackerrank.com/challenges/py-set-mutations/problem

# -------------------------------------- Task --------------------------------------:
# You are given a set "A" and "N" number of other sets. These "N" number of sets have to perform some specific mutation operations on set "A".
# Your task is to execute those operations and print the sum of elements from set "A".
# ----------------------------------------------------------------------------------


num_a = int(input())
a = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    operation, num = input().split()
    ls = list(map(int, input().split()))
    eval(f"a.{operation}({ls})")
    
print(sum(a))