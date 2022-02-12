# https://www.hackerrank.com/challenges/finding-the-percentage/problem

# -------------------------------------- Task --------------------------------------:
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# ----------------------------------------------------------------------------------


n = int(input()) # number of students
student_marks = {}

# adding students' records to dictionary
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

scores = student_marks[query_name] # getting query student's scores
score = 0

# adding up all scores
for x in scores:
    score += x

# calculating average and printing it correct to 2 decimal places
average = score / len(scores)
print(f"{average:.2f}")