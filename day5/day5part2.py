filename = "day5.in"

NUM_STACKS = 0
EMPTY_SPACE = " "
stacks: list[list[int]] = []

def conductInstruction(moveAmt: int, moveFromStack: int, moveToStack: int) -> None:
    global stacks
    toMove: list[str] = stacks[moveFromStack][:moveAmt]
    stacks[moveFromStack] = stacks[moveFromStack][moveAmt:]
    stacks[moveToStack] = toMove + stacks[moveToStack]

def parseStack(s: str) -> None:
    global stacks
    for i in range(NUM_STACKS):
        stackVal: str = s[1 + i * 4]
        if (stackVal == EMPTY_SPACE):
            continue
        stacks[i].append(stackVal)

def parseInstruction(s: str) -> None:
    splitLine: list[str] = s.split()
    moveAmt: int = int(splitLine[1])
    moveFromStack: int = int(splitLine[3]) - 1
    moveToStack: int = int(splitLine[5]) - 1
    conductInstruction(moveAmt, moveFromStack, moveToStack)

def parseLine(s: str, isStack: bool) -> None:
    if (isStack):
        parseStack(s)
    else:
        parseInstruction(s)

with open(filename, 'r') as f:
    isStack: bool = True
    for line in f:
        if (NUM_STACKS == 0):
            NUM_STACKS = len(line) // 4
            stacks = [[] for i in range(NUM_STACKS)]
        if (line == "\n" or line[1] == "1"):
            isStack = False
            continue
        parseLine(line[:-1], isStack)

finalOutput: str = ""

for i in range(NUM_STACKS):
    if (stacks[i]):
        finalOutput += stacks[i][0]

print("Final message: " + finalOutput)