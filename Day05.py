import re

pattern = "move (\d+) from (\d+) to (\d+)"
state = [["H", "T", "Z", "D"],
         ["Q", "R", "W", "T", "G", "C", "S"],
         ["P", "B", "F", "Q", "N", "R", "C", "H"],
         ["L", "C", "N", "F", "H", "Z"],
         ["G", "L", "F", "Q", "S"],
         ["V", "P", "W", "Z", "B", "R", "C", "S"],
         ["Z", "F", "J"],
         ["D", "L", "V", "Z", "R", "H", "Q"],
         ["B", "H", "G", "N", "F", "Z", "L", "D"]]
#state = [["Z", "N"], ["M", "C", "D"], ["P"]]

def Day05_P1():
    print(state)
    with open("Day05_Input.txt") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                print(match.groups())
                for i in range(int(match.groups()[0])):
                    grab = state[int(match.groups()[1]) - 1].pop()
                    print(grab)
                    state[int(match.groups()[2]) - 1].append(grab)
                #grab = state[int(match.groups()[1]) - 1][len(state[int(match.groups()[1]) - 1])-int(match.groups()[0]):]
                #state[int(match.groups()[2]) - 1].append(grab if len(grab) == 1 else grab.reverse())
                print(state)
            #state[match.groups()[3]]
    result = ""
    for i in range(len(state)):
        result += state[i][-1]
    print(result)

def Day05_P2():
    print(state)
    with open("Day05_Input.txt") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                print(match.groups())
                grab = state[int(match.groups()[1]) - 1][len(state[int(match.groups()[1]) - 1])-int(match.groups()[0]):]
                print(grab)
                for i in range(int(match.groups()[0])):
                    state[int(match.groups()[1]) - 1].pop()
                state[int(match.groups()[2]) - 1] += grab
                # grab = state[int(match.groups()[1]) - 1][len(state[int(match.groups()[1]) - 1])-int(match.groups()[0]):]
                # state[int(match.groups()[2]) - 1].append(grab if len(grab) == 1 else grab.reverse())
                print(state)
            # state[match.groups()[3]]
    result = ""
    for i in range(len(state)):
        result += state[i][-1]
    print(result)

