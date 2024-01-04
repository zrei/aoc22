from enum import Enum
import ast

class Outcome(Enum):
    PASS = 0
    FAIL = 1
    INCONCLUSIVE = 2

filename = "day13.in"

def helper(comparison1: list, comparison2: list) -> Outcome:
    for i in range(len(comparison1)):
        if i >= len(comparison2):
            return Outcome.FAIL
        if type(comparison1[i]) == int and type(comparison2[i]) == int:
            if comparison1[i] == comparison2[i]:
                continue
            elif comparison1[i] < comparison2[i]: 
                return Outcome.PASS
            elif comparison1[i] > comparison2[i]:
                return Outcome.FAIL
        elif (type(comparison1[i]) == list and type(comparison2[i]) == list):
            result: Outcome = helper(comparison1[i], comparison2[i])
            if (result == Outcome.INCONCLUSIVE):
                continue
            return result
        elif (type(comparison1[i]) == list and type(comparison2[i]) == int):
            result: Outcome = helper(comparison1[i], [comparison2[i]])
            if (result == Outcome.INCONCLUSIVE):
                continue
            return result
        elif (type(comparison1[i]) == int and type(comparison2[i]) == list):
            result: Outcome = helper([comparison1[i]], comparison2[i])
            if (result == Outcome.INCONCLUSIVE):
                continue
            return result
    if len(comparison1) == len(comparison2):
        return Outcome.INCONCLUSIVE
    return Outcome.PASS

totalSum: int = 0

with open(filename, "r") as f:
    firstList: list = []
    secondList: list = []
    index: int = 0
    indice: int = 1
    for line in f:
        if line == "\n":
            continue
        if index % 2 == 0:
            firstList = ast.literal_eval(line[:-1])
        else:
            secondList = ast.literal_eval(line[:-1])
            if helper(firstList, secondList) == Outcome.PASS:
                totalSum += indice
            indice += 1
        index += 1

print("Total sum: " + str(totalSum))