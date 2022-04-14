# https://www.hackerrank.com/challenges/designer-door-mat/problem

# -------------------------------------- Task --------------------------------------:
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#   - Mat size must be 'N' x 'M'. ('N' is an odd natural number, and 'M' is 3 times 'N'.)
#   - The design should have 'WELCOME' written in the center.
#   - The design pattern should only use |, . and - characters.
# ----------------------------------------------------------------------------------


N, M = map(int, input().split())

x = int((N - 1) / 2)
y = 1

# printing first half
for _ in range(x):
    print((".|." * y).center(M, '-'))
    y += 2
    
print("WELCOME".center(M, '-'))

# printing second half
for _ in range(x):
    y -= 2
    print((".|." * y).center(M, '-'))