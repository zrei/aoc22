from collections import deque

filename = "day12.in"

STARTING_STEP = "S"
ENDING_STEP = "E"

numRows: int = 0
numCols: int = 0

def canTravel(prevStep: str, nextStep: str) -> bool:
    if prevStep == STARTING_STEP:
        prevStep = 'a' 
    if nextStep == ENDING_STEP:
        nextStep = 'z'
    return ord(nextStep) - ord(prevStep) <= 1

def outOfBounds(row: int, col: int) -> bool:
    return row < 0 or row >= numRows or col < 0 or col >= numCols

grid: list[str] = []

with open(filename, "r") as f:
    for line in f:
        grid.append(line[:-1])

numRows = len(grid)
numCols = len(grid[0])

def findPoint(grid: list[str], point: str) -> tuple[int]:
    for row in range(numRows):
        for col in range(numCols):
            if grid[row][col] == point:
                return (row, col)
            
def bfs(grid: list[str], startingPoint: tuple[int], endingPoint: tuple[int]) -> int:
    encounteredPoints: dict = {}
    frontier = deque()
    frontier.append((startingPoint, STARTING_STEP, 0))
    while (frontier):
        point, prevStep, pathLength = frontier.popleft()
        if (outOfBounds(point[0], point[1])):
            continue
        if (not canTravel(prevStep, grid[point[0]][point[1]])):
            continue
        if point in encounteredPoints:
            continue
        encounteredPoints[point] = 1
        if (point == endingPoint):
            return pathLength
        frontier.append(((point[0] + 1, point[1]), grid[point[0]][point[1]], pathLength + 1))
        frontier.append(((point[0] - 1, point[1]), grid[point[0]][point[1]], pathLength + 1))
        frontier.append(((point[0], point[1] + 1), grid[point[0]][point[1]], pathLength + 1))
        frontier.append(((point[0], point[1] - 1), grid[point[0]][point[1]], pathLength + 1))

print("Shortest length: " + str(bfs(grid, findPoint(grid, STARTING_STEP), findPoint(grid, ENDING_STEP))))