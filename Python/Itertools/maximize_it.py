# https://www.hackerrank.com/challenges/maximize-it/problem

# -------------------------------------- Task --------------------------------------:
# You are given a function "f(X) = X^2". You are also given "K" lists. The "i-th" list consists of "N" elements. 
# You have to pick one element from each list so that the value from the equation below is maximized:
# S = (f(X1) + f(X2) + ... + f(Xk)) % M
# "Xi" denotes the element picked from the "i-th" list. Find the maximized value "S_max" obtained. "%" denotes the modulo operator.

# Note that you need to take exactly one element from each list, not necessarily the largest element. 
# You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
# ----------------------------------------------------------------------------------


from itertools import product

K, M = map(int, input().split())

lists = []
s_max = 0

# Add all values with a power of 2
for _ in range(K):
    ls = list(map(lambda x: int(x) ** 2, input().split()))[1:]
    lists.append(ls)

# Create all possible permutations
perm = list(product(*lists))

# Find biggest value
for i in perm:
    x = sum(i) % M
    
    if x > s_max:
        s_max = x
        
print(s_max)