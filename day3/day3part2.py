from collections import Counter

filename = "day3.in"

ASCII_CAPITAL_A = 65
ASCII_SMALL_A = 97

def getPriority(char: str) -> int:
    if (ord(char) >= ASCII_SMALL_A):
        return ord(char) - ASCII_SMALL_A + 1
    else:
        return ord(char) - ASCII_CAPITAL_A + 27
    
def findCommon(bag1: str, bag2: str, bag3: str) -> int:
    firstBagLetters = Counter(bag1)
    secondBagLetters = Counter(bag2)
    thirdBagLetters = Counter(bag3)
    for l in firstBagLetters.keys():
        if l in secondBagLetters and l in thirdBagLetters:
            return getPriority(l)

totalSum: int = 0

with open(filename, 'r') as f:
    firstLine: str = ""
    secondLine: str = ""
    thirdLine: str = ""
    index: int = 0
    for line in f:
        if index % 3 == 0:
            firstLine = line[:-1]
        elif index % 3 == 1:
            secondLine = line[:-1]
        elif index % 3 == 2:
            thirdLine = line[:-1]
            totalSum += findCommon(firstLine, secondLine, thirdLine)
        index += 1

print("Total: " + str(totalSum))