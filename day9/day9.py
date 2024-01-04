filename = "day9.in"

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"

class rope:
    headPosition: tuple[int] = (0, 0)
    tailPosition: tuple[int] = (0, 0)
    tailVisitedPositions: dict = {tailPosition: 1}
    numVisitedPositions: int = 1

    def getDistance(self) -> tuple[int]:
        return (self.headPosition[0] - self.tailPosition[0], self.headPosition[1] - self.tailPosition[1])
    
    def moveRight(self) -> None:
        self.headPosition = (self.headPosition[0], self.headPosition[1] + 1)
        self.adjustTail()

    def moveLeft(self) -> None:
        self.headPosition = (self.headPosition[0], self.headPosition[1] - 1)
        self.adjustTail()

    def moveUp(self) -> None:
        self.headPosition = (self.headPosition[0] - 1, self.headPosition[1])
        self.adjustTail()

    def moveDown(self) -> None:
        self.headPosition = (self.headPosition[0] + 1, self.headPosition[1])
        self.adjustTail()

    def adjustTail(self) -> None:
        print(self.headPosition, self.tailPosition)
        distance: tuple[int] = self.getDistance()
        if abs(distance[0]) < 2 and abs(distance[1]) < 2:
            print("Tail will not move")
            return
        if distance[0] == 2 and distance[1] == 0:
            self.tailPosition = (self.tailPosition[0] + 1, self.tailPosition[1])
        elif distance[0] == 2 and distance[1] == 1:
            self.tailPosition = (self.tailPosition[0] + 1, self.tailPosition[1] + 1)
        elif distance[0] == 2 and distance[1] == -1:
            self.tailPosition = (self.tailPosition[0] + 1, self.tailPosition[1] - 1)
        elif distance[0] == -2 and distance[1] == 0:
            self.tailPosition = (self.tailPosition[0] - 1, self.tailPosition[1])
        elif distance[0] == -2 and distance[1] == 1:
            self.tailPosition = (self.tailPosition[0] - 1, self.tailPosition[1] + 1)
        elif distance[0] == -2 and distance[1] == -1:
            self.tailPosition = (self.tailPosition[0] - 1, self.tailPosition[1] - 1)
        elif distance[0] == 0 and distance[1] == 2:
            self.tailPosition = (self.tailPosition[0], self.tailPosition[1] + 1)
        elif distance[0] == 0 and distance[1] == -2:
            self.tailPosition = (self.tailPosition[0], self.tailPosition[1] - 1)
        elif distance[0] == 1 and distance[1] == 2:
            self.tailPosition = (self.tailPosition[0] + 1, self.tailPosition[1] + 1)
        elif distance[0] == 1 and distance[1] == -2:
            self.tailPosition = (self.tailPosition[0] + 1, self.tailPosition[1] - 1)
        elif distance[0] == -1 and distance[1] == 2:
            self.tailPosition = (self.tailPosition[0] - 1, self.tailPosition[1] + 1)
        elif distance[0] == -1 and distance[1] == -2:
            self.tailPosition = (self.tailPosition[0] - 1, self.tailPosition[1] - 1)
        print(self.tailPosition)
        if self.tailPosition not in self.tailVisitedPositions:
            self.numVisitedPositions += 1
            self.tailVisitedPositions[self.tailPosition] = 1

def performInstruction(line: str, r: rope) -> None:
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