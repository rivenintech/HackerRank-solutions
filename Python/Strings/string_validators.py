# https://www.hackerrank.com/challenges/string-validators/problem

# -------------------------------------- Task --------------------------------------:
# You are given a string 'S'.
# Your task is to find out if the string 'S' contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
# ----------------------------------------------------------------------------------


s = input()
result = ["False"] * 5 # default values

for i in range(len(s)):
    if s[i].isalnum():
        result[0] = "True"
     
    if s[i].isalpha():
        result[1] = "True"
        
    if s[i].isdigit():
        result[2] = "True"

    if s[i].islower():
        result[3] = "True"

    if s[i].isupper():
        result[4] = "True"

print("\n".join(result))