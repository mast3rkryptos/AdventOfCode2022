import re

def CheckSignalStrength(cycle, value):
    if cycle >= 20 and (cycle - 20) % 40 == 0:
        CheckSignalStrength.result += cycle * value
        print(cycle, CheckSignalStrength.result)
CheckSignalStrength.result = 0

def Day10_P1():
    pattern = "(\w+)\s*?([\-\d]+)?$"
    x = 1
    cycle = 1
    with open("Day10_Input.txt") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                #print(match.groups())
                if match.groups()[0] == "addx":
                    CheckSignalStrength(cycle, x)
                    cycle += 1
                    CheckSignalStrength(cycle, x)
                    cycle += 1
                    x += int(match.groups()[1])
                else:
                    CheckSignalStrength(cycle, x)
                    cycle += 1

def DrawPixel(cycle, crt, value):
    if (cycle - 1) % 40 == 0:
        newRow = []
        crt.append(newRow)
    crt[-1].append("#" if (value - 1) <= (cycle - 1) % 40 <= (value + 1) else ".")

def Day10_P2():
    pattern = "(\w+)\s*?([\-\d]+)?$"
    x = 1
    cycle = 1
    crt = []
    with open("Day10_Input.txt") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                # print(match.groups())
                if match.groups()[0] == "addx":
                    DrawPixel(cycle, crt, x)
                    cycle += 1
                    DrawPixel(cycle, crt, x)
                    cycle += 1
                    x += int(match.groups()[1])
                else:
                    DrawPixel(cycle, crt, x)
                    cycle += 1
    for row in crt:
        print("".join(row))