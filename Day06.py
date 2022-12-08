import re

pattern = "move (\d+) from (\d+) to (\d+)"

def Day06_P1():
    with open("Day06_Input.txt") as f:
        for line in f:
            for i in range(0, len(line)-4):
                allUnique = True
                for j in range(i, i+4):
                    for k in range(j+1, i+4):
                        allUnique &= line[j] != line[k]
                        #print(j, k, line[j], line[k])
                #print(line, line[i:i+4], allUnique)
                if allUnique:
                    print(line.strip(), i+4)
                    break

def Day06_P2():
    with open("Day06_Input.txt") as f:
        for line in f:
            for i in range(0, len(line) - 14):
                allUnique = True
                for j in range(i, i + 14):
                    for k in range(j + 1, i + 14):
                        allUnique &= line[j] != line[k]
                        # print(j, k, line[j], line[k])
                # print(line, line[i:i+4], allUnique)
                if allUnique:
                    print(line.strip(), i + 14)
                    break

