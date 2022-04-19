# https://www.hackerrank.com/challenges/py-the-captains-room/problem

# -------------------------------------- Task --------------------------------------:
# One fine day, a finite number of tourists come to stay at the hotel. The Captain was given a separate room, and the rest were given one room per group.
# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists.
# The room numbers will appear "K" times per group except for the Captain's room. Mr. Anant needs you to help him find the Captain's room number.
# ----------------------------------------------------------------------------------


gr_size = int(input())
rooms = list(map(int, input().split()))

answer = (sum(set(rooms)) * gr_size - sum(rooms)) / (gr_size - 1)

print(int(answer))