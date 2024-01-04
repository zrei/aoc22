filename = "day9.in"

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"

NUM_KNOTS = 9

class rope:
    positions: list[tuple[int]] = [(0, 0) for i in range(NUM_KNOTS + 1)]
    tailVisitedPositions: dict = {positions[-1]: 1}
    numVisitedPositions: int = 1

    def getDistance(self, knotNum1: int, knotNum2: int) -> tuple[int]:
        knot1: tuple[int] = self.positions[knotNum1]
        knot2: tuple[int] = self.positions[knotNum2]
        return (knot1[0] - knot2[0], knot1[1] - knot2[1])
    
    def moveRight(self) -> None:
        print("Moving right")
        head: tuple[int] = self.positions[0]
        self.positions[0] = (head[0], head[1] + 1)
        self.adjustKnots()

    def moveLeft(self) -> None:
        print("moving left")
        head: tuple[int] = self.positions[0]
        self.positions[0] = (head[0], head[1] - 1)
        self.adjustKnots()

    def moveUp(self) -> None:
        print("moving up")
        head: tuple[int] = self.positions[0]
        self.positions[0] = (head[0] - 1, head[1])
        self.adjustKnots()

    def moveDown(self) -> None:
        print("moving down")
        head: tuple[int] = self.positions[0]
        self.positions[0] = (head[0] + 1, head[1])
        self.adjustKnots()

    def adjustKnots(self) -> None:
        for i in range(NUM_KNOTS):
            #print(i, i + 1)
            #print(self.positions)
            self.adjustTail(i, i + 1)
        #print(self.positions)
        if self.positions[-1] not in self.tailVisitedPositions:
            self.numVisitedPositions += 1
            self.tailVisitedPositions[self.positions[-1]] = 1
    
    def adjustTail(self, knotNum1: int, knotNum2: int) -> None:
        distance: tuple[int] = self.getDistance(knotNum1, knotNum2)
        if abs(distance[0]) < 2 and abs(distance[1]) < 2:
            #print("Knot will not move: " + str(knotNum1) + ", " + str(knotNum2))
            #print(distance[0], distance[1])
            return
        tail: tuple[int] = self.positions[knotNum2]
        if (abs(distance[0]) > abs(distance[1])):
            if distance[0] > 0:
                self.positions[knotNum2] = (tail[0] + distance[0] - 1, tail[1] + distance[1])
            else:
                self.positions[knotNum2] = (tail[0] + distance[0] + 1, tail[1] + distance[1])
        elif (abs(distance[0]) < abs(distance[1])):
            if distance[1] > 0:
                self.positions[knotNum2] = (tail[0] + distance[0], tail[1] + distance[1] - 1)
            else:
                self.positions[knotNum2] = (tail[0] + distance[0], tail[1] + distance[1] + 1)
        else:
            if distance[0] > 0 and distance[1] > 0:
                self.positions[knotNum2] = (tail[0] + distance[0] - 1, tail[1] + distance[1] - 1)
            elif distance[0] > 0 and distance[1] < 0:
                self.positions[knotNum2] = (tail[0] + distance[0] - 1, tail[1] + distance[1] + 1)
            elif distance[0] < 0 and distance[1] > 0:
                self.positions[knotNum2] = (tail[0] + distance[0] + 1, tail[1] + distance[1] - 1)
            elif distance[0] < 0 and distance[1] < 0:
                self.positions[knotNum2] = (tail[0] + distance[0] + 1, tail[1] + distance[1] - 1)
            else:
                print("Uncaught case?")
            #print("EQUAL??? " + str(knotNum1) + ", " + str(knotNum2))
            #print(distance)
        '''if distance[0] == 0 and distance[1] > 0:
            self.positions[knotNum2] = (tail[0], tail[1] + (abs(distance[1]) - 1))
        elif distance[0] == 0 and distance[1] < 0:
            self.positions[knotNum2] = (tail[0], tail[1] - (abs(distance[1]) - 1))
        elif distance[1] == 0 and distance[0] < 0:
            self.positions[knotNum2] = (tail[0] - (abs(distance[0]) - 1), tail[1])
        elif distance[1] == 0 and distance[0] > 0:
            self.positions[knotNum2] = (tail[0] + (abs(distance[0]) - 1), tail[1])
        elif abs(distance[0]) > abs(distance[1]):
            if distance[0] > 0 and distance[1] < 0:
                self.positions[knotNum2] = (tail[0] + (abs(distance[0]) - 1), tail[1] - (abs(distance[1]) - 1))
            elif distance[0] > 0 and distance[1] > 0:
                self.positions[knotNum2] = (tail[0] + (abs(distance[0]) - 1), tail[1] + (abs(distance[1]) - 1))
            elif distance[0] < 0 and distance[1] < 0:
                self.positions[knotNum2] = (tail[0] - (abs(distance[0]) - 1), tail[1] - (abs(distance[1]) - 1))
            elif distance[0] < 0 and distance[1] > 0:
                self.positions[knotNum2] = (tail[0] - (abs(distance[0]) - 1), tail[1] + (abs(distance[1]) - 1))
        else:
            print("UHHHH: " + str(distance))'''
        '''if distance[0] >= 2 and distance[1] == 0:
            self.positions[knotNum2] = (tail[0] + 1, tail[1])
        elif distance[0] >= 2 and distance[1] == 1:
            self.positions[knotNum2] = (tail[0] + 1, tail[1] + 1)
        elif distance[0] >= 2 and distance[1] == -1:
            self.positions[knotNum2] = (tail[0] + 1, tail[1] - 1)
        elif distance[0] >= 2 and distance[1] >= 2:
            self.positions[knotNum2] = (tail[0] + 1, tail[1] - 1)
        elif distance[0] == 2 and distance[1] <= -2:
            self.positions[knotNum2] = (tail[0] + 1, tail[1] - 1)
        elif distance[0] == -2 and distance[1] == 0:
            self.positions[knotNum2] = (tail[0] - 1, tail[1])
        elif distance[0] == -2 and distance[1] == 1:
            self.positions[knotNum2] = (tail[0] - 1, tail[1] + 1)
        elif distance[0] == -2 and distance[1] == -1:
            self.positions[knotNum2] = (tail[0] - 1, tail[1] - 1)
        elif distance[0] == -2 and distance[1] == 2:
            self.positions[knotNum2] = (tail[0] - 1, tail[1] + 1)
        elif distance[0] == -2 and distance[1] == -2:
            self.positions[knotNum2] = (tail[0] - 1, tail[1] - 1)
        elif distance[0] == 0 and distance[1] == 2:
            self.positions[knotNum2] = (tail[0], tail[1] + 1)
        elif distance[0] == 0 and distance[1] == -2:
            self.positions[knotNum2] = (tail[0], tail[1] - 1)
        elif distance[0] == 1 and distance[1] == 2:
            self.positions[knotNum2] = (tail[0] + 1, tail[1] + 1)
        elif distance[0] == 1 and distance[1] == -2:
            self.positions[knotNum2] = (tail[0] + 1, tail[1] - 1)
        elif distance[0] == -1 and distance[1] == 2:
            self.positions[knotNum2] = (tail[0] - 1, tail[1] + 1)
        elif distance[0] == -1 and distance[1] == -2:
            self.positions[knotNum2] = (tail[0] - 1, tail[1] - 1)'''
        
        
print("ATTEMPT 5")
def performInstruction(line: str, r: rope) -> None:
    print(line)
    splitLine = line.split()
    if (splitLine[0] == UP):
        for i in range(int(splitLine[1])):
            r.moveUp()
    elif (splitLine[0] == DOWN):
        for i in range(int(splitLine[1])):
            r.moveDown()
    elif (splitLine[0] == RIGHT):
        for i in range(int(splitLine[1])):
            r.moveRight()
    elif (splitLine[0] == LEFT):
        for i in range(int(splitLine[1])):
            r.moveLeft()

with open(filename, "r") as f:
    r: rope = rope()
    for line in f:
        performInstruction(line[:-1], r)
    print("Number of visited positions: " + str(r.numVisitedPositions))