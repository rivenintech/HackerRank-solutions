# https://www.hackerrank.com/challenges/triangle-quest-2/problem

# -------------------------------------- Task --------------------------------------:
# You are given a positive integer "N". Your task is to print a palindromic triangle of size "N". Example (size 5):
# 1
# 121
# 12321
# 1234321
# 123454321

# Can you do it using only arithmetic operations, a single for loop and print statement?
# ----------------------------------------------------------------------------------


for i in range(1, int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10 ** i // 9) ** 2)