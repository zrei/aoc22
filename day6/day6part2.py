filename = "day6.in"

PERIOD_LENGTH = 14

def findFirstMarker(s: str) -> int:
    lp: int = 0
    rp: int = 0
    encounteredCharacters: dict = {}
    while (rp < len(s)):
        if (s[rp] not in encounteredCharacters):
            encounteredCharacters[s[rp]] = 0
        encounteredCharacters[s[rp]] += 1
        if (s[rp] in encounteredCharacters and encounteredCharacters[s[rp]] > 1):
            while (True):
                encounteredCharacters[s[lp]] -= 1
                lp += 1
                if (encounteredCharacters[s[lp - 1]] == 1):
                    break
        elif (rp - lp + 1 == PERIOD_LENGTH):
            return rp + 1
        rp += 1
            
with open(filename, "r") as f:
    for line in f:
        print("The first marker appearance is at " + str(findFirstMarker(line[:-1])))