# https://www.hackerrank.com/challenges/python-string-formatting/problem

# -------------------------------------- Task --------------------------------------:
# Given an integer, 'n', print the following values for each integer 'i' from '1' to 'n': Decimal, Octal, Hexadecimal (capitalized), Binary.

# The four values must be printed on a single line in the order specified above for each 'i' from '1' to 'number'.
# Each value should be space-padded to match the width of the binary value of 'number' and the values should be separated by a single space.
# ----------------------------------------------------------------------------------


def print_formatted(number):
    width = len(f"{number:b}") # checking number's width (in binary)
    
    for i in range(1, number + 1): # creating a range of numbers
        converted = [j.rjust(width) for j in [f'{i}', f'{i:o}', f'{i:X}', f'{i:b}']] # converting number to different systems
        print(" ".join(converted)) # printing joined values
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)