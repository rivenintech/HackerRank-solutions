# https://www.hackerrank.com/challenges/the-minion-game/problem

# -------------------------------------- Task --------------------------------------:
# Both players are given the same string, "S". Both players have to make substrings using the letters of the string "S".
# Stuart has to make words starting with consonants. Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# Your task is to determine the winner of the game and their score.
# Note: Vowels are only defined as AEIOU. In this problem, "Y" is not considered a vowel.
# ----------------------------------------------------------------------------------


vowels = set(["A", "E", "I", "O", "U"])

def minion_game(string):
    stuart, kevin = 0, 0
    length = len(string)

    for i in range(length):
        if string[i] not in vowels: # stuart (substring doesn't start with vowel)
            stuart += length - i
        else: # kevin
            kevin += length - i

    if stuart == kevin: # draw
        print("Draw")
    elif stuart > kevin: # stuart wins
        print(f"Stuart {stuart}")
    else: # kevin wins
        print(f"Kevin {kevin}")

if __name__ == '__main__':
    s = input()
    minion_game(s)