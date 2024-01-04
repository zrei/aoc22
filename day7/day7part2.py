filename = "day7.in"

BASH_IDENTIFIER = "$"
TOTAL_DISK_SPACE = 70000000
REQUIRED_UNUSED_SPACE = 30000000

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
    dirSum[dirList[-1]] += int(splitLine[0])

with open(filename, "r") as f:
    dirList: list[str] = []
    for line in f:
        if (isBash(line)):
            processBash(line, dirList)
        else:
            processDirLine(line, dirList)
    for i in range(len(dirList) - 1, 0, -1):
        dirSum[dirList[i - 1]] += dirSum[dirList[i]]
    unusedSpace: int = TOTAL_DISK_SPACE - dirSum[dirList[0]]
    spaceToFree: int = REQUIRED_UNUSED_SPACE - unusedSpace
    dirSpace: list[int] = list(dirSum.values())
    dirSpace.sort()
    for space in dirSpace:
        if space >= spaceToFree:
            print("Smallest space: " + str(space))
            break 

