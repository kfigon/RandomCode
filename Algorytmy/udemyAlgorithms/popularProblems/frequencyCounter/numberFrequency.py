from typing import List, Dict

# given 2 positive integers
# find 2 numbers with same frequency of digits

# O(n)

def convertAndCount(a: int) -> Dict[str, int]:
    x = str(a)
    out: Dict[str, int] = {}
    for i in x:
        out[i] = 1 if i not in out else out[i] + 1
    return out

def sameFrequency(a: int, b:int) -> bool:
    freqA = convertAndCount(a)
    freqB = convertAndCount(b)
    for key in freqA:
        if key not in freqB or freqA[key] != freqB[key]:
            return False
    return True

assert sameFrequency(182,281) == True
assert sameFrequency(34,14) == False
assert sameFrequency(3589578, 5879385) == True
assert sameFrequency(22,222) == False