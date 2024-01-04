filename = "day4.in"

PAIR_SEPARATOR = ","
RANGE_SEPARATOR = "-"

def getRange(range: str) -> tuple[int]:
    first, second = range.split(RANGE_SEPARATOR)
    return (int(first), int(second))

def getRanges(s: str) -> tuple[tuple[int]]:
    first, second = s.split(PAIR_SEPARATOR)
    return (getRange(first), getRange(second))

def isOverlapping(s: str) -> bool:
    first, second = getRanges(s)
    if (first[0] >= second[0] and first[0] <= second[1]): 
        return True
    elif (first[1] >= second[0] and first[1] <= second[1]):
        return True
    elif (second[0] >= first[0] and second[0] <= first[1]):
        return True
    elif (second[1] >= first[0] and second[1] <= first[1]):
        return True
    return False

totalPairs: int = 0

with open(filename, "r") as f:
    for line in f:
        if (isOverlapping(line[:-1])):
            totalPairs += 1

print("Total number of pairs: " + str(totalPairs))