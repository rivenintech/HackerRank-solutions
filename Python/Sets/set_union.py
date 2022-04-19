# https://www.hackerrank.com/challenges/py-set-union/problem

# -------------------------------------- Task --------------------------------------:
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper.
# The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
# ----------------------------------------------------------------------------------


e = int(input())
english = set(map(int, input().split()))
f = int(input())
french = set(map(int, input().split()))

print(len(english.union(french)))