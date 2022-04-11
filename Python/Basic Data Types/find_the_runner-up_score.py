# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# -------------------------------------- Task --------------------------------------:
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given 'n' scores. Store them in a list and find the score of the runner-up.
# ----------------------------------------------------------------------------------


# Finding second biggest value without sorting
n = int(input())
arr = map(int, input().split())

scores = set(arr) # using "set" instead of "list" to remove multiple identical values
scores.remove(max(scores)) # finding biggest number and removing it

print(max(scores)) # now the biggest number is the second biggest one in the array