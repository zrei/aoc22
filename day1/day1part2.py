filename = "day1.in"

maxCalory: int = 0
nextMaxCalory: int = 0
nextNextMaxCalory: int = 0

def redefineMax(newMax: int) -> None:
    global maxCalory
    global nextMaxCalory
    global nextNextMaxCalory
    if (newMax > maxCalory):
        nextNextMaxCalory = nextMaxCalory
        nextMaxCalory = maxCalory
        maxCalory = newMax
    elif (newMax > nextMaxCalory):
        nextNextMaxCalory = nextMaxCalory
        nextMaxCalory = newMax
    elif (newMax > nextNextMaxCalory):
        nextNextMaxCalory = newMax

with open(filename, "r") as f:
    caloryCount: int = 0
    for line in f:
        if line == "\n":
            redefineMax(caloryCount)
            caloryCount = 0
        else:
            caloryCount += int(line[:-1])
    redefineMax(caloryCount)

print(maxCalory, nextMaxCalory, nextNextMaxCalory)
print("Max calory count " + str(maxCalory + nextMaxCalory + nextNextMaxCalory))
