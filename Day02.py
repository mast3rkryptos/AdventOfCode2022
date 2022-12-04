import re

def Day02_P1():
    score = 0
    with open("Day02_Input.txt") as f:
        for line in f:
            opponent = ord(line[0]) - 64
            player = ord(line[2]) - 87
            if opponent == player:
                score += 3 + player
            elif (opponent == 1 and player == 2) or (opponent == 2 and player == 3) or (opponent == 3 and player == 1):
                score += 6 + player
            else:
                score += player
    print(score)

def Day02_P2():
    score = 0
    with open("Day02_Input.txt") as f:
        for line in f:
            opponent = ord(line[0]) - 64
            player = -1
            if line[2] == "X":
                player = 3 if (opponent - 1) == 0 else opponent - 1
            elif line[2] == "Y":
                player = opponent
            else:
                player = (opponent % 3) + 1
            if opponent == player:
                score += 3 + player
            elif (opponent == 1 and player == 2) or (opponent == 2 and player == 3) or (opponent == 3 and player == 1):
                score += 6 + player
            else:
                score += player
    print(score)

