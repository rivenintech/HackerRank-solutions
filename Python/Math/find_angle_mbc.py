# https://www.hackerrank.com/challenges/find-angle/problem

# -------------------------------------- Task --------------------------------------:
# ABC is a right triangle, "90°" at "B". "ABC" = "90°". Point "M" is the midpoint of hypotenuse "AC".
# You are given the lengths "AB" and "BC". Your task is to fimd "MBC" angle in degrees.
# ----------------------------------------------------------------------------------


import math

ab = int(input())
bc = int(input())

h = math.sqrt(ab ** 2 + bc ** 2)
h /= 2
n = bc / 2

answer = round(math.degrees(math.acos(n / h)))

print(f"{answer}\N{DEGREE SIGN}")