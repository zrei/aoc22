filename = "day8.in"

numRows: int = 0
numCols: int = 0
forest: list[str] = []

with open(filename, "r") as f:
    for line in f:
        forest.append(line[:-1])

numRows = len(forest)
numCols = len(forest[0])

numVisible: int = 0
numVisible += numCols * 2
numVisible += (numRows - 2) * 2

print("Num edges: " + str(numVisible))
encounteredCoords: dict = {}

for row in range(1, numRows - 1):
    maxTree: int = int(forest[row][0])
    for i in range(1, numCols - 1):
        print("1: " + str(row) + ", " +str(i))
        tree: int = int(forest[row][i])
        print(tree, maxTree)
        if tree > maxTree and (row, i) not in encounteredCoords:
            print(row, i)
            numVisible += 1
            encounteredCoords[(row, i)] = 1
        maxTree = max(maxTree, tree)
    maxTree = int(forest[row][-1])
    for i in range(numCols - 2, 0, -1):
        print("2: " + str(row) + ", " +str(i))
        tree: int = int(forest[row][i])
        print(tree, maxTree)
        if int(tree) > maxTree and (row, i) not in encounteredCoords:
            print(row, i)
            numVisible += 1
            encounteredCoords[(row, i)] = 1
        maxTree = max(maxTree, tree)

for col in range(1, numCols - 1):
    maxTree: int = int(forest[0][col])
    for i in range(1, numRows - 1):
        print("3: " + str(i) + ", " +str(col))
        tree: int = int(forest[i][col])
        print(tree, maxTree)
        if tree > maxTree and (i, col) not in encounteredCoords:
            print(i, col)
            numVisible += 1
            encounteredCoords[(i, col)] = 1
        maxTree = max(maxTree, tree)
    maxTree = int(forest[-1][col])
    for i in range(numRows - 2, 0, -1):
        print("4: " + str(i) + ", " + str(col))
        tree: int = int(forest[i][col])
        print(tree, maxTree)
        if int(tree) > maxTree and (i, col) not in encounteredCoords:
            print(i, col)
            numVisible += 1
            encounteredCoords[(i, col)] = 1
        maxTree = max(maxTree, tree)

print("Num visible: " + str(numVisible))