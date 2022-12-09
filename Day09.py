import re

def Day09_P1():
    pattern = "(\w) (\d+)"
    headLoc = {"x":0, "y":0}
    tailLoc = {"x":0, "y":0}
    tailHistory = [(0,0)]
    with open("Day09_Input.txt") as f:
        for line in f:
            print(line.strip())
            match = re.match(pattern, line)
            if match:
                for i in range(int(match.groups()[1])):
                    # Move head
                    headLoc["x"] += 1 if match.groups()[0] == "R" else 0
                    headLoc["x"] -= 1 if match.groups()[0] == "L" else 0
                    headLoc["y"] += 1 if match.groups()[0] == "U" else 0
                    headLoc["y"] -= 1 if match.groups()[0] == "D" else 0
                    print("Head:", headLoc)
                    # Move tail
                    if abs(headLoc["x"] - tailLoc["x"]) > 1 or abs(headLoc["y"] - tailLoc["y"]) > 1:
                        tailLoc["x"] += 1 if headLoc["x"] - tailLoc["x"] > 0 else 0
                        tailLoc["x"] -= 1 if headLoc["x"] - tailLoc["x"] < 0 else 0
                        tailLoc["y"] += 1 if headLoc["y"] - tailLoc["y"] > 0 else 0
                        tailLoc["y"] -= 1 if headLoc["y"] - tailLoc["y"] < 0 else 0
                    print("Tail:", tailLoc)
                    tailHistory.append((tailLoc["x"], tailLoc["y"])) if (tailLoc["x"], tailLoc["y"]) not in tailHistory else None
            print()
    print(len(tailHistory))

def Day09_P2():
    pattern = "(\w) (\d+)"
    knotLoc = []
    for i in range(10):
        knotLoc.append({"x":0, "y":0})
    tailHistory = [(0,0)]
    with open("Day09_Input.txt") as f:
        for line in f:
            print(line.strip())
            match = re.match(pattern, line)
            if match:
                for i in range(int(match.groups()[1])):
                    # Move head
                    knotLoc[0]["x"] += 1 if match.groups()[0] == "R" else 0
                    knotLoc[0]["x"] -= 1 if match.groups()[0] == "L" else 0
                    knotLoc[0]["y"] += 1 if match.groups()[0] == "U" else 0
                    knotLoc[0]["y"] -= 1 if match.groups()[0] == "D" else 0
                    print("Head:", knotLoc[0])
                    # Move the rest
                    for i in range(1, 10):
                        if abs(knotLoc[i-1]["x"] - knotLoc[i]["x"]) > 1 or abs(knotLoc[i-1]["y"] - knotLoc[i]["y"]) > 1:
                            knotLoc[i]["x"] += 1 if knotLoc[i-1]["x"] - knotLoc[i]["x"] > 0 else 0
                            knotLoc[i]["x"] -= 1 if knotLoc[i-1]["x"] - knotLoc[i]["x"] < 0 else 0
                            knotLoc[i]["y"] += 1 if knotLoc[i-1]["y"] - knotLoc[i]["y"] > 0 else 0
                            knotLoc[i]["y"] -= 1 if knotLoc[i-1]["y"] - knotLoc[i]["y"] < 0 else 0
                        print("Tail:", knotLoc[i])
                    tailHistory.append((knotLoc[-1]["x"], knotLoc[-1]["y"])) if (knotLoc[-1]["x"], knotLoc[-1]["y"]) not in tailHistory else None
            print()
    print(len(tailHistory))