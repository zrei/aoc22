filename = "day1.in"

maxCalory: int = 0

with open(filename, "r") as f:
    caloryCount: int = 0
    for line in f:
        if line == "\n":
            maxCalory = max(caloryCount, maxCalory)
            caloryCount = 0
        else:
            caloryCount += int(line[:-1])
    maxCalory = max(caloryCount, maxCalory)

print("Max calory count " + str(maxCalory))
