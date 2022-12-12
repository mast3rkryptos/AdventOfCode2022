class Node:
    def __init__(self, id, elevation):
        self.id = id
        self.elevation = elevation
        self.connections = []

    def __str__(self):
        return f"Node {self.id}\n  Elevation: {self.elevation}\n  Connections: {self.connections}\n"

    def AddConnection(self, id, elevation):
        self.connections.append((id, elevation - self.elevation))
        return

    def Navigate(self, nodes, currentPathLength):
        for connection in self.connections:
            if connection[1] <= 1:
                nodes[connection[0]].Navigate(nodes)

def Day12_P1():
    heightmap = []
    nodes = {}
    start = None
    end = None
    with open("Day12_Input.txt") as f:
        for line in f:
            heightmap.append(line.strip())
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            nodes[f"{i},{j}"] = Node(f"{i},{j}", ord(heightmap[i][j]) - 97 if heightmap[i][j] != "S" and heightmap[i][j] != "E" else (0 if heightmap[i][j] == "S" else 26))
            if heightmap[i][j] == "S":
                start = nodes[f"{i},{j}"]
            elif heightmap[i][j] == "E":
                end = nodes[f"{i},{j}"]

    start.Navigate(nodes, 0)
    print(start, end)
