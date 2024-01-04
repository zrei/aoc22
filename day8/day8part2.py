filename = "day8.in"

numRows: int = 0
numCols: int = 0
forest: list[str] = []

with open(filename, "r") as f:
    for line in f:
        forest.append(line[:-1])

numRows = len(forest)
numCols = len(forest[0])

maxScenicScore: int = 0

def getScenicScore(row: int, col: int) -> int:
    tree: int = forest[row][col]

    # check up
    upScore: int = 0
    for i in range(row - 1, -1, -1):
        upScore += 1
        if (forest[i][col] >= tree):
            break
    
    # check down
    downScore: int = 0
    for i in range(row + 1, numRows):
        downScore += 1
        if (forest[i][col] >= tree):
            break
        
    # check left
    leftScore: int = 0
    for i in range(col - 1, -1, -1):
        leftScore += 1
        if (forest[row][i] >= tree):
            break

    # check right
    rightScore: int = 0
    for i in range(col + 1, numCols):
        rightScore += 1
        if (forest[row][i] >= tree):
            break
        
    return upScore * downScore * leftScore * rightScore

for row in range(1, numRows - 1):
    for col in range(1, numCols - 1):
        print(row, col, getScenicScore(row, col))
        maxScenicScore = max(maxScenicScore, getScenicScore(row, col))

print("Max scenic score: " + str(maxScenicScore))