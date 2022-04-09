# https://www.hackerrank.com/challenges/swap-case/problem

# -------------------------------------- Task --------------------------------------:
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# ----------------------------------------------------------------------------------


def swap_case(s):
    new_string = ""
    
    # looping through each letter of string
    for x in s:
        if x.islower():
            x = x.upper()
        else:
            x = x.lower()
            
        new_string += x
        
    return new_string # you can also just use 'return s.swapcase()' - which is a builtin function

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)