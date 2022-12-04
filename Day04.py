import re
def Day04_P1():
    sum = 0
    with open("Day04_Input.txt") as f:
        for line in f:
            stripline = line.strip()
            splitlines = stripline.split(",")

            if (int(splitlines[0].split("-")[0]) <= int(splitlines[1].split("-")[0]) and int(splitlines[0].split("-")[1]) >= int(splitlines[1].split("-")[1])) or \
                    (int(splitlines[0].split("-")[0]) >= int(splitlines[1].split("-")[0]) and int(splitlines[0].split("-")[1]) <= int(splitlines[1].split("-")[1])):
                sum += 1
    print(sum)

def Day04_P2():
    sum = 0
    with open("Day04_Input.txt") as f:
        for line in f:
            stripline = line.strip()
            splitlines = stripline.split(",")

            if (int(splitlines[0].split("-")[0]) <= int(splitlines[1].split("-")[0]) and int(splitlines[0].split("-")[1]) >= int(splitlines[1].split("-")[1])) or \
                    (int(splitlines[0].split("-")[0]) >= int(splitlines[1].split("-")[0]) and int(splitlines[0].split("-")[1]) <= int(splitlines[1].split("-")[1])) or \
                    (int(splitlines[0].split("-")[0]) >= int(splitlines[1].split("-")[0]) and int(splitlines[0].split("-")[0]) <= int(splitlines[1].split("-")[1])) or \
                    (int(splitlines[0].split("-")[1]) >= int(splitlines[1].split("-")[0]) and int(splitlines[0].split("-")[1]) <= int(splitlines[1].split("-")[1])):
                sum += 1
    print(sum)

