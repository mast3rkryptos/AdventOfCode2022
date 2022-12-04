alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def Day03_P1():
    sum = 0
    with open("Day03_Input.txt") as f:
        for line in f:
            stripline = line.strip()
            half1 = sorted(stripline[0:int(len(stripline)/2)])
            half2 = sorted(stripline[int(len(stripline)/2):])
            match = ""
            for i in range(len(half1)):
                for j in range(len(half2)):
                    if half1[i] == half2[j]:
                        match = half1[i]
                        break
                if match != "":
                    break
            sum += alphabet.index(match) + 1
    print(sum)

def Day03_P2():
    sum = 0
    with open("Day03_Input.txt") as f:
        group = []
        for line in f:
            stripline = line.strip()
            if len(group) != 3:
                group.append(stripline)
            if len(group) == 3:
                match = ""
                for i in range(len(group[0])):
                    for j in range(len(group[1])):
                        for k in range(len(group[2])):
                            if group[0][i] == group[1][j] and group[0][i] == group[2][k]:
                                match = group[0][i]
                                break
                        if match != "":
                            break
                    if match != "":
                        break
                sum += alphabet.index(match) + 1
                group = []
    print(sum)

