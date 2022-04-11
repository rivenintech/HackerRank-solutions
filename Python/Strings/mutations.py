# https://www.hackerrank.com/challenges/python-mutations/problem

# -------------------------------------- Task --------------------------------------:
# Read a given string, change the character at a given index and then print the modified string.
# ----------------------------------------------------------------------------------


def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    
    return "".join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)