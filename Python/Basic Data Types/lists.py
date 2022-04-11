# https://www.hackerrank.com/challenges/python-lists/problem

# -------------------------------------- Task --------------------------------------:
# Commands: 'insert i e', 'print', 'remove e', 'append e', 'sort', 'pop', 'reverse'

# Initialize your list and read in the value of 'n' followed by 'n' lines of commands where each command will be of the '7' types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.
# ----------------------------------------------------------------------------------


N = int(input())
ls = []

for i in range(N):
    cmd = input().split()
    
    if cmd[0] == ("insert"):
        ls.insert(int(cmd[1]), int(cmd[2]))
    
    elif cmd[0] == "print":
        print(ls)

    elif cmd[0] in ["append", "remove"]: # grouping these commands together - their syntax is similar
        eval(f"ls.{cmd[0]}({cmd[1]})")
        
    elif cmd[0] in ["sort", "pop", "reverse"]: # grouping these commands together - their syntax is similar
        eval(f"ls.{cmd[0]}()")