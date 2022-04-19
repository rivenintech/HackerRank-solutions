# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# -------------------------------------- Task --------------------------------------:
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper.
# Your task is to find the total number of students who have subscribed to both newspapers.
# ----------------------------------------------------------------------------------


e = int(input())
english = set(map(int, input().split()))
f = int(input())
french = set(map(int, input().split()))

print(len(english.intersection(french)))