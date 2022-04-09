# https://www.hackerrank.com/challenges/py-if-else/problem

# -------------------------------------- Task --------------------------------------:
# Given an integer, 'n', perform the following conditional actions:
# - If 'n' is odd, print "Weird"
# - If 'n' is even and in the inclusive range of 2 to 5, print "Not Weird"
# - If 'n' is even and in the inclusive range of 6 to 20, print "Weird"
# - If 'n' is even and greater than 20, print "Not Weird"
# ----------------------------------------------------------------------------------


n = int(input())

# if the reminder of division by 2 is 1 it's odd
if n % 2 == 1:
    print("Weird")
else:
    # if in range 2 - 5
    if n in range(2, 6):
        print("Not Weird")

    # if in range 6 - 20
    elif n in range(6, 21):
        print("Weird")
        
    elif n > 20:
        print("Not Weird")