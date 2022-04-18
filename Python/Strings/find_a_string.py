# https://www.hackerrank.com/challenges/find-a-string/problem

# -------------------------------------- Task --------------------------------------:
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

# Sample Input: "ABCDCDC", "CDC"
# Sample Output: "2"
# ----------------------------------------------------------------------------------


def count_substring(string, sub_string):
    counter = 0

    for i in range(len(string) - len(sub_string) + 1): # max search length
        if string[i:(i + len(sub_string))] == sub_string:
            counter += 1

    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)