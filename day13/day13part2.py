from enum import Enum
import ast
import functools

class Outcome(Enum):
    PASS = 0
    FAIL = 1
    INCONCLUSIVE = 2

filename = "day13.in"

DIVIDER_1 = [[2]]
DIVIDER_2 = [[6]]

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

packetList: list = []

def customCmp(packet1, packet2) -> int:
    result = helper(packet1, packet2) 
    if (result == Outcome.PASS):
        return -1
    elif (result == Outcome.FAIL):
        return 1
    elif (result == Outcome.INCONCLUSIVE):
        return 0

finalAns: int = 1

with open(filename, "r") as f:
    for line in f:
        if line == "\n":
            continue
        packetList.append(ast.literal_eval(line[:-1]))
    packetList.append(DIVIDER_1)
    packetList.append(DIVIDER_2)
    packetList.sort(key=functools.cmp_to_key(customCmp))
    for idx, i in enumerate(packetList):
        if i == DIVIDER_1 or i == DIVIDER_2:
            finalAns *= idx + 1

print("Final answer: " + str(finalAns))