# https://www.hackerrank.com/challenges/compress-the-string/problem

# -------------------------------------- Task --------------------------------------:
# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools.
# You are given a string "S". Suppose a character 'c' occurs consecutively "X" times in the string.
# Replace these consecutive occurrences of the character 'c' with "(X, c)" in the string.
# ----------------------------------------------------------------------------------


from itertools import groupby

s = input()
  
for k, g in groupby(s):
    res = [int(k), len(list(g))]
    res = (res[1], res[0])
    
    print(res, end=" ")