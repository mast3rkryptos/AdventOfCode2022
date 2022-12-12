pathLengths = []

def Navigate(current, destination, heightmap, currentPathLength):
    if current == destination:
        pathLengths.append(currentPathLength)
    else:
        currentPathLength += 1
        if current[0] > 0 and 0 <= ord(heightmap[current[0]][current[1]]) - ord(heightmap[current[0]-1][current[1]]) <= 1:
            Navigate((current[0]-1, current[1]), destination, heightmap, currentPathLength)
        if current[0] < len(heightmap) - 1 and 0 <= ord(heightmap[current[0]][current[1]]) - ord(heightmap[current[0]+1][current[1]]) <= 1:
            Navigate((current[0]+1, current[1]), destination, heightmap, currentPathLength)
        if current[1] > 0 and 0 <= ord(heightmap[current[0]][current[1]]) - ord(heightmap[current[0]-1][current[1]-1]) <= 1:
            Navigate((current[0], current[1]-1), destination, heightmap, currentPathLength)
        if current[1] < len(heightmap[current[0]]) - 1 and 0 <= ord(heightmap[current[0]][current[1]]) - ord(heightmap[current[0]][current[1]+1]) <= 1:
            Navigate((current[0], current[1]+1), destination, heightmap, currentPathLength)


def Day12_P1():
    heightmap = []
    nodes = {}
    start = None
    end = None
    with open("Day12_Input.txt") as f:
        for line in f:
            heightmap.append(line.strip())
    # Find the starting and ending locations
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if heightmap[i][j] == "S":
                start = (i, j)
                heightmap[i] = heightmap[i].replace("S", "a")
            elif heightmap[i][j] == "E":
                end = (i, j)
                heightmap[i] = heightmap[i].replace("E", "z")


    Navigate(end, start, heightmap, 0)
    print(start, end, pathLengths)
