# https://www.hackerrank.com/challenges/list-comprehensions/problem

# -------------------------------------- Task --------------------------------------:
# You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k)
# on a 3D grid where the sum of i + j + k is not equal to n.
# ----------------------------------------------------------------------------------

# taking input and changing it to "int" type
x = int(input())
y = int(input())
z = int(input())
n = int(input())

ls = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(ls)