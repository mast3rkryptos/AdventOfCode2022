def Day01_P1():
    elves = []
    with open("Day01_Input.txt") as f:
        sum = 0
        for line in f:
            stripline = line.strip("\n")
            if len(stripline) != 0:
                sum += int(stripline)
            else:
                elves.append(sum)
                sum = 0
    print(max(elves))

def Day01_P2():
    elves = []
    with open("Day01_Input.txt") as f:
        sum = 0
        for line in f:
            stripline = line.strip("\n")
            if len(stripline) != 0:
                sum += int(stripline)
            else:
                elves.append(sum)
                sum = 0
        elves.append(sum)
    print(sorted(elves))
    print(sorted(elves)[-1] + sorted(elves)[-2] + sorted(elves)[-3])
