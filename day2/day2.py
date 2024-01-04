filename = "day2.in"

ROCK_1 = 'A'
PAPER_1 = 'B'
SCISSORS_1 = 'C'

ROCK_2 = 'X'
PAPER_2 = 'Y'
SCISSORS_2 = 'Z'

def isDraw(play1: str, play2: str) -> bool:
    return (play1 == ROCK_1 and play2 == ROCK_2) or (play1 == SCISSORS_1 and play2 == SCISSORS_2) or (play1 == PAPER_1 and play2 == PAPER_2)

def scoreOutcome(play1: str, play2: str) -> int:
    if (isDraw(play1, play2)):
        return 3
    elif (play1 == ROCK_1 and play2 == SCISSORS_2):
        return 0
    elif (play1 == ROCK_1 and play2 == PAPER_2):
        return 6
    elif (play1 == SCISSORS_1 and play2 == PAPER_2):
        return 0
    elif (play1 == SCISSORS_1 and play2 == ROCK_2):
        return 6
    elif (play1 == PAPER_1 and play2 == ROCK_2):
        return 0
    elif (play1 == PAPER_1 and play2 == SCISSORS_2):
        return 6

def playOutcome(play: str) -> int:
    if (play == ROCK_2):
        return 1
    elif (play == SCISSORS_2):
        return 3
    elif (play == PAPER_2):
        return 2

totalScore: int = 0

with open(filename, "r") as f:
    for line in f:
        splitLine = line.split()
        totalScore += playOutcome(splitLine[1]) + scoreOutcome(splitLine[0], splitLine[1])

print("Final score: " + str(totalScore))