# https://www.hackerrank.com/challenges/nested-list/problem

# -------------------------------------- Task --------------------------------------:
# Given the names and grades for each student in a class of 'n' students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# ----------------------------------------------------------------------------------


records = list()
scores = set()

# adding students to set
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    scores.add(score)
    
scores.remove(min(scores)) # removing lowest grade
second_lowest = min(scores) # second lowest grade is now the lowest one in set

names = [x[0] for x in records if x[1] == second_lowest] # adding names if the grade is the second lowest one
names.sort() # sorting names alphabetically

# printing names
for i in names:
    print(i)