# https://www.hackerrank.com/challenges/find-a-string/problem

# -------------------------------------- Task --------------------------------------:
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

# Sample Input: "ABCDCDC", "CDC"
# Sample Output: "2"
# ----------------------------------------------------------------------------------


def count_substring(string, sub_string):
    counter = 0
    
    # looping through a string
    for i in range(len(string)):
        if string[i] == sub_string[0]: # if first letter matches sub_string's first letter
            counter += 1
            
            for j in range(len(sub_string)):
                try:
                    if string[i + j] != sub_string[j]: # if any letter doesn't match -> end loop
                        counter -= 1
                        break
                except IndexError: # if it goes beyond string boundary
                    counter -= 1
                    break
        
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)