filename = "day7.in"

BASH_IDENTIFIER = "$"
MAX_LIMIT = 100000

totalSum: int = 0
dirSum: dict = {}
dirAppearance: dict = {}

def isNumber(char: str) -> bool:
    return ord(str) - ord("0") >= 0 and ord(str) - ord("0") <= 10

def isBash(line: str) -> bool:
    return line[0] == BASH_IDENTIFIER

def processBash(line: str, dirList: list[str]) -> None:
    global totalSum
    global dirSum
    global dirAppearance
    splitLine: list[str] = line.split()
    if splitLine[1] == "cd":
        if splitLine[2] == "..":
            print("Current directory: " + dirList[-1] + ", " + str(dirSum[dirList[-1]]))
            if dirSum[dirList[-1]] <= MAX_LIMIT:
                totalSum += dirSum[dirList[-1]]
                print("Adding to total sum for " + dirList[-1] + ", " + str(dirSum[dirList[-1]]))
            print("Recursively adding to " + dirList[-2])
            dirSum[dirList[-2]] += dirSum[dirList[-1]]
            dirList.pop()
        else:
            if splitLine[2] not in dirAppearance:
                dirAppearance[splitLine[2]] = 0
            dirAppearance[splitLine[2]] += 1
            dirList.append(splitLine[2] + str(dirAppearance[splitLine[2]]))
            dirSum[dirList[-1]] = 0

def processDirLine(line: str, dirList: list[str]) -> None:
    splitLine: list[str] = line.split()
    if splitLine[0] == "dir":
        return
    print("Adding to: " + dirList[-1] + ", " + splitLine[0])
    dirSum[dirList[-1]] += int(splitLine[0])

with open(filename, "r") as f:
    dirList: list[str] = []
    for line in f:
        if (isBash(line)):
            processBash(line, dirList)
        else:
            processDirLine(line, dirList)
    for i in range(len(dirList) - 1, 0, -1):
        print(dirList[i] + " " + str(dirSum[dirList[i]]))
        if dirSum[dirList[i]] <= MAX_LIMIT:
            print("Adding to total sum for " + dirList[i] + ", " + str(dirSum[dirList[i]]))
            totalSum += dirSum[dirList[i]]
        dirSum[dirList[i - 1]] += dirSum[dirList[i]]
    print(dirList[0] + " " + str(dirSum[dirList[0]]))
    if dirSum[dirList[0]] <= MAX_LIMIT:
        print("Adding to total sum for " + dirList[0] + ", " + str(dirSum[dirList[0]]))
        totalSum += dirSum[dirList[0]]

print("Final sum: " + str(totalSum))