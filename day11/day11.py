filename = "day11.in"

VARIABLE = "old"
MULTIPLY = "*"
ADD = "+"
MINUS = "-"
DIVIDE = "/"

class monkey:

    def __init__(self):
        self.itemAnxietyLevels: list[int] = []
        self.operation = lambda x : x + 1
        self.testNum: int = 0
        self.falseThrower: int = 0
        self.trueThrower: int = 0
        self.numTimesInspected: int = 0

    def addItem(self, item: int) -> None:
        self.itemAnxietyLevels.append(item)

    def changeBooleanRule(self, testNum: int) -> None:
        self.testNum = testNum

    def test(self, num: int) -> bool:
        return num % self.testNum == 0

    def changeOperation(self, newOperation) -> None:
        self.operation = newOperation

    def setFalseTarget(self, target: int) -> None:
        self.falseThrower = target
        
    def setTrueTarget(self, target: int) -> None:
        self.trueThrower = target

    def performOperation(self, anxietyLevel: int) -> bool:
        return self.operation(anxietyLevel)
    
    def getTarget(self, hasPassed: bool) -> int:
        if hasPassed:
            return self.trueThrower
        else:
            return self.falseThrower

    def oneRound(self, monkeyList: list['monkey']) -> None:
        print("Number of items: " + str(len(self.itemAnxietyLevels)))
        for i in self.itemAnxietyLevels:
            self.numTimesInspected += 1
            monkeyList[self.getTarget(self.test(self.performOperation(i) // 3))].addItem(self.performOperation(i) // 3)
        self.itemAnxietyLevels.clear()

def createDoubleVariableLambda(operator: str):
    if (operator == MULTIPLY):
        return lambda x : x * x
    elif (operator == DIVIDE):
        return lambda x : x // x
    elif operator == ADD:
        return lambda x : x + x
    elif operator == MINUS:
        return lambda x : x - x

def createLeftVariableLambda(operator: str, val: int):
    if (operator == MULTIPLY):
        return lambda x : x * val
    elif (operator == DIVIDE):
        return lambda x : x // val
    elif operator == ADD:
        return lambda x : x + val
    elif operator == MINUS:
        return lambda x : x - val
    
def createRightVariableLambda(operator: str, val: int):
    if (operator == MULTIPLY):
        return lambda x : val * x
    elif (operator == DIVIDE):
        return lambda x : val // x
    elif operator == ADD:
        return lambda x : val + x
    elif operator == MINUS:
        return lambda x : val - x
    
def createNoVariableLambda(operator: str, val1: int, val2: int):
    if (operator == MULTIPLY):
        return lambda x : val1 * val2
    elif (operator == DIVIDE):
        return lambda x : val1 // val2
    elif operator == ADD:
        return lambda x : val1 + val2
    elif operator == MINUS:
        return lambda x : val1 - val2

monkeyList: list[monkey] = []

with open(filename, "r") as f:
    for line in f:
        if line == "\n":
            continue
        splitLine = line[:-1].strip().split()
        if splitLine[0] == "Monkey":
            monkeyList.append(monkey())
        elif splitLine[0] == "Starting":
            for i in splitLine[2:]:
                s = i.split(",")
                monkeyList[-1].addItem(int(s[0]))
        elif splitLine[0] == "Operation:":
            firstOperator = splitLine[3:][0]
            secondOperator = splitLine[3:][1]
            thirdOperator = splitLine[3:][2]
            if (firstOperator == VARIABLE and thirdOperator != VARIABLE):
                monkeyList[-1].changeOperation(createLeftVariableLambda(secondOperator, int(thirdOperator)))
            elif (firstOperator != VARIABLE and thirdOperator == VARIABLE):
                monkeyList[-1].changeOperation(createRightVariableLambda(secondOperator, int(firstOperator)))
            elif (firstOperator == VARIABLE and thirdOperator == VARIABLE):
                monkeyList[-1].changeOperation(createDoubleVariableLambda(secondOperator))
            elif (firstOperator != VARIABLE and thirdOperator != VARIABLE):
                monkeyList[-1].changeOperation(createNoVariableLambda(secondOperator, int(firstOperator), int(thirdOperator)))
        elif splitLine[0] == "Test:":
            monkeyList[-1].changeBooleanRule(int(splitLine[-1]))
        elif splitLine[0] + " " + splitLine[1] == "If true:":
            monkeyList[-1].setTrueTarget(int(splitLine[-1]))
        elif splitLine[0] + " " + splitLine[1] == "If false:":    
            monkeyList[-1].setFalseTarget(int(splitLine[-1]))

print("Number of items")
for m in monkeyList:
    print(len(m.itemAnxietyLevels))
maxInspectionTime: int = 0
nextMaxInspectionTime: int = 0
for i in range(20):
    print("Round " + str(i))
    for m in monkeyList:
        print("A monkey!")
        m.oneRound(monkeyList)
        if m.numTimesInspected > maxInspectionTime:
            nextMaxInspectionTime = maxInspectionTime
            maxInspectionTime = m.numTimesInspected
        elif m.numTimesInspected > nextMaxInspectionTime:
            nextMaxInspectionTime = m.numTimesInspected
    print("")

print("Final answer: " + str(maxInspectionTime * nextMaxInspectionTime))

