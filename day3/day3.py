from collections import Counter

filename = "day3.in"

ASCII_CAPITAL_A = 65
ASCII_SMALL_A = 97

def getPriority(char: str) -> int:
    if (ord(char) >= ASCII_SMALL_A):
        return ord(char) - ASCII_SMALL_A + 1
    else:
        return ord(char) - ASCII_CAPITAL_A + 27
    
def findCommon(bag: str) -> int:
    midPoint: int = len(bag) // 2
    firstHalf: str = bag[:midPoint]
    secondHalf: str = bag[midPoint:]
    firstHalfLetters = Counter(firstHalf)
    secondHalfLetters = Counter(secondHalf)
    for l in firstHalfLetters.keys():
        if l in secondHalfLetters:
            return getPriority(l)

totalSum: int = 0

with open(filename, 'r') as f:
    for line in f:
        totalSum += findCommon(line[:-1])

print("Total: " + str(totalSum))