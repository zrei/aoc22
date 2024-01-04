filename = "day2.in"

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

def scoreOutcome(outcome: str) -> int:
    if (outcome == LOSE):
        return 0
    elif (outcome == DRAW):
        return 3
    elif (outcome == WIN):
        return 6

def playOutcome(play: str, outcome: str) -> int:
    if ((play == ROCK and outcome == DRAW) or (play == PAPER and outcome == LOSE) or (play == SCISSORS and outcome == WIN)):
        return 1
    elif ((play == SCISSORS and outcome == DRAW) or (play == PAPER and outcome == WIN) or (play == ROCK and outcome == LOSE)):
        return 3
    elif ((play == PAPER and outcome == DRAW) or (play == SCISSORS and outcome == LOSE) or (play == ROCK and outcome == WIN)):
        return 2

totalScore: int = 0

with open(filename, "r") as f:
    for line in f:
        splitLine = line.split()
        totalScore += playOutcome(splitLine[0], splitLine[1]) + scoreOutcome(splitLine[1])

print("Final score: " + str(totalScore))