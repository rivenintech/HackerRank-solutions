# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

# -------------------------------------- Task --------------------------------------:
# You have a non-empty set "S", and you have to execute "N" commands given in "N" lines. The commands will be "pop", "remove" and "discard".
# ----------------------------------------------------------------------------------


n = int(input())
s = set(map(int, input().split()))

def check(command):
    if command.startswith("pop"): 
        s.pop()
    else:
        command_name, value = command.split(" ")
        
        if command_name == "remove":
            s.remove(int(value))
        elif command_name == "discard":
            s.discard(int(value))

for _ in range(int(input())):
    check(input())
    
print(sum(s))