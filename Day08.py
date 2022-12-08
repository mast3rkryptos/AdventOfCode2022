import re

def Day08_P1():
    map = []
    visibleCount = 0
    with open("Day08_Input.txt") as f:
        for line in f:
           map.append(line.strip())
    visibleCount = 2 * (len(map) + len(map[0])) - 4
    for i in range(1, len(map)-1):
        for j in range(1, len(map[i])-1):
            value = map[i][j]
            isHidden = True
            # Check North
            tempHidden = False
            k = i - 1
            while k != -1 and not tempHidden:
                tempHidden |= map[i][j] <= map[k][j]
                k -= 1
            isHidden &= tempHidden
            # Check South
            tempHidden = False
            k = i + 1
            while k != len(map) and not tempHidden:
                tempHidden |= map[i][j] <= map[k][j]
                k += 1
            isHidden &= tempHidden
            # Check West
            tempHidden = False
            k = j - 1
            while k != -1 and not tempHidden:
                tempHidden |= map[i][j] <= map[i][k]
                k -= 1
            isHidden &= tempHidden
            # Check East
            tempHidden = False
            k = j + 1
            while k != len(map[i]) and not tempHidden:
                tempHidden |= map[i][j] <= map[i][k]
                k += 1
            isHidden &= tempHidden
            visibleCount += 0 if isHidden else 1
    print(visibleCount)

def Day08_P2():
    map = []
    visibleCount = 0
    with open("Day08_Input.txt") as f:
        for line in f:
           map.append(line.strip())
    for i in range(1, len(map)-1):
        for j in range(1, len(map[i])-1):
            tempVisibleCount = 1
            # Check North
            dirVisibleCount = 0
            k = i - 1
            while k != -1:
                dirVisibleCount += 1
                if map[i][j] <= map[k][j]:
                    break
                k -= 1
            tempVisibleCount *= dirVisibleCount
            # Check South
            dirVisibleCount = 0
            k = i + 1
            while k != len(map):
                dirVisibleCount += 1
                if map[i][j] <= map[k][j]:
                    break
                k += 1
            tempVisibleCount *= dirVisibleCount
            # Check West
            dirVisibleCount = 0
            k = j - 1
            while k != -1:
                dirVisibleCount += 1
                if map[i][j] <= map[i][k]:
                    break
                k -= 1
            tempVisibleCount *= dirVisibleCount
            # Check East
            dirVisibleCount = 0
            k = j + 1
            while k != len(map[i]):
                dirVisibleCount += 1
                if map[i][j] <= map[i][k]:
                    break
                k += 1
            tempVisibleCount *= dirVisibleCount
            visibleCount = tempVisibleCount if tempVisibleCount > visibleCount else visibleCount
    print(visibleCount)