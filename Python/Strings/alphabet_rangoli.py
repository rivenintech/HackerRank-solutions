# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# -------------------------------------- Task --------------------------------------:
# You are given an integer, "N". Your task is to print an alphabet rangoli of size "N". 

# Sample Input: 5

# Sample Output:
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
# ----------------------------------------------------------------------------------


import string

alphabet = string.ascii_lowercase

def print_rangoli(size):
    width = (size * 2 - 1) * 2 - 1

    # Looping with range from "-size" to "size" (e.g. "-2" -> "2")
    for i in range(size * -1 + 1, size):
        row = ""
        x = size - abs(i)

        # Looping with range from "-x" to "x" (e.g. "-2" -> "2")
        for j in range(x * -1 + 1, x):
            row += alphabet[abs(j) + abs(i)] + " "

        # striping, replacing " " with "-" and adding rest of "-" to match the width
        print(row.strip().replace(" ", "-").center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)