filename = "day10.in"

MAX_CYCLE = 220
PERIOD_LENGTH = 40
PERIOD_START = 20

NOOP = "noop"
ADDX = "addx"

totalSum: int = 0
currX: int = 1
cycleNum: int = 1
instructions: list[tuple[int]] = []
# tuple is (x increase amount, cycle time)

with open(filename, "r") as f:
    for line in f:
        splitLine: str = line[:-1].split()
        if splitLine[0] == NOOP:
            instructions.append((0, 1))
        elif splitLine[0] == ADDX:
            instructions.append((int(splitLine[1]), 2))

while (cycleNum <= MAX_CYCLE):
    if (instructions):
        increaseAmt, cycleTime = instructions[0]
        while (cycleTime == 0):
            currX += increaseAmt
            instructions.pop(0)
            if (increaseAmt != 0):
                print("Adding " + str(increaseAmt) + " on " + str(cycleNum))
            if (instructions):
                increaseAmt, cycleTime = instructions[0]
            else:
                cycleTime = -1
        if (instructions):
            instructions[0] = (increaseAmt, cycleTime - 1)
    if cycleNum >= PERIOD_START and (cycleNum - PERIOD_START) % PERIOD_LENGTH == 0:
        totalSum += currX * cycleNum
        print(cycleNum, currX, totalSum)
    cycleNum += 1

print("Total sum: " + str(totalSum))