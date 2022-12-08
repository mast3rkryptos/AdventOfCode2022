import re

result1 = 0

class Directory:
    result2 = []
    def __init__(self, name, parent):
        self.name = name
        self.files = {}
        self.directories = {}
        self.size = -1
        self.parent = parent

    def AddFile(self, name, size):
        if name not in self.files.keys():
            self.files[name] = int(size)
        return

    def AddDirectory(self, name):
        if name not in self.directories.keys():
            newDirectory = Directory(name, self)
            self.directories[name] = newDirectory
        return

    def GetParent(self):
        return self.parent

    def GetSubDirectory(self, name):
        ret = None
        if name == "..":
            ret = self.GetParent()
        else:
            ret = self.directories[name]
        return ret

    def GetSize(self):
        global result1
        size = 0
        if self.size != -1:
            size = self.size
        else:
            for file in self.files.values():
                size += file
            for directory in self.directories.values():
                size += directory.GetSize()
        self.size = size
        # Code to get the final answer for AoC
        if self.size <= 100000:
            result1 += self.size
        Directory.result2.append(self.size)
        return self.size

def Day07():
    with open("Day07_Input.txt") as f:
        commandPattern = "\$ (\w+)\s*([/\.\w]*)"
        dirPattern = "dir (\w+)"
        filePattern = "(\d+) ([\.\w]+)"
        root = Directory("/", None)
        current = root
        for line in f:
            match = re.match(commandPattern, line)
            if match:
                print("Command: ", match.groups())
                if match.groups()[0] == "cd":
                    if match.groups()[1] == "/":
                        current = root
                    else:
                        current = current.GetSubDirectory(match.groups()[1])
                continue
            match = re.match(dirPattern, line)
            if match:
                print("Directory: ", match.groups())
                current.AddDirectory(match.groups()[0])
                continue
            match = re.match(filePattern, line)
            if match:
                print("File: ", match.groups())
                current.AddFile(match.groups()[1], match.groups()[0])
                continue
        rootSize = root.GetSize()
        neededSize = 30000000 - (70000000 - rootSize)
        r2 = 0
        Directory.result2.sort()
        for size in Directory.result2:
            if size >= neededSize:
                r2 = size
                break
        print(result1, r2)

