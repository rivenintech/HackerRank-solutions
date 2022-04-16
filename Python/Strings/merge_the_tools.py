# https://www.hackerrank.com/challenges/merge-the-tools/problem

# -------------------------------------- Task --------------------------------------:
# Split "string" into equal parts of length "k". Remove any subsequent occurrences of non-distinct characters.

# Example Input: string = AABCAAADA, k = 3

# Example Output:
# AB
# CA
# AD
# ----------------------------------------------------------------------------------


from textwrap import wrap

def merge_the_tools(string, k):
    splited = wrap(string, k) # split string
    
    # Loop through all strings
    for x in splited:
        print("".join(dict.fromkeys(x))) # using dict to remove duplicates, but also preserve order

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)