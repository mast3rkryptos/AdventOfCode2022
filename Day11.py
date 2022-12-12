import re
import math

class Monkey:
    masterDivisor = 1

    def __init__(self, id):
        self.id = id
        self.items = []
        self.operation = ()
        self.test = []
        self.inspectCount = 0

    def __str__(self):
        return f"Monkey {self.id}\n  Items: {self.items}\n  Operation: {self.operation}\n  Test: {self.test}\n  Inspect Count: {self.inspectCount}"

    def AddItem(self, item):
        self.items.append(item)

    def SetOperation(self, operation):
        self.operation  = operation
    
    def SetTest(self, test):
        self.test = test

    def TakeTurn(self, barrel):
        print(f"Monkey {self.id}")
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.inspectCount += 1
            print(f"  Monkey inspects an item with a worry level of {item}")
            item = item * self.operation[1] if self.operation[0] == "*" else (item + self.operation[1] if self.operation[0] == "+" else item * item)
            print(f"    Worry level changes to {item}")
            #item = math.floor(item / 3)
            #print(f"    Monkey gets bored with item. Worry level is divided by 3 to {item}")
            if item % self.test[0] == 0:
                print(f"    Current worry level is divisible by {self.test[0]}")
                barrel[self.test[1]].AddItem(item % Monkey.masterDivisor)
                print(f"    Item with worry level {item} is thrown to monkey {self.test[1]}.")
            else:
                print(f"    Current worry level is not divisible by {self.test[0]}")
                barrel[self.test[2]].AddItem(item % Monkey.masterDivisor)
                print(f"    Item with worry level {item} is thrown to monkey {self.test[2]}.")

def Day11_P1():
    with open("Day11_Input.txt") as f:
        stage = 0
        barrel = []
        test = []
        for line in f:
            if stage == 0:
                match = re.search("(\d+)", line)
                if match:
                    barrel.append(Monkey(int(match.groups()[0])))
            elif stage == 1:
                match = re.findall("\d+", line)
                if match:
                    for m in match:
                        barrel[-1].AddItem(int(m))
            elif stage == 2:
                match = re.search("([\*\+])\s(old|\d+)", line)
                if match:
                    if match.groups()[1] == "old":
                        barrel[-1].SetOperation(("^", 2))
                    else:
                        barrel[-1].SetOperation((match.groups()[0], int(match.groups()[1])))
            elif stage == 3 or stage == 4 or stage == 5:
                match = re.search("(\d+)", line)
                if match:
                    test.append(int(match.groups()[0]))
                    if stage == 5:
                        barrel[-1].SetTest(test)
                        test = []
            stage = (stage + 1) % 7
    for monkey in barrel:
        Monkey.masterDivisor *= monkey.test[0]
        print(monkey)
    for round in range(0, 10000):
        print(round)
        for monkey in barrel:
            monkey.TakeTurn(barrel)
    for monkey in barrel:
        print(monkey)
