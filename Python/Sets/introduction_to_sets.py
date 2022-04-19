# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

# -------------------------------------- Task --------------------------------------:
# Ms. Gabriel Williams is a botany professor at District College.
# One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# Formula: Average = Sum of Distinct Heights / Total Number of Distinct Heights
# ----------------------------------------------------------------------------------


def average(array):
    arr = set(array)
    return sum(arr) / len(arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)