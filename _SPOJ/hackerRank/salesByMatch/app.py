# https://www.hackerrank.com/challenges/sock-merchant/problem
from typing import List, Dict


def calcPairs(tab: List[int]) -> int:
    sockMap: Dict[int, int] = {}
    for v in tab:
        if v in sockMap:
            sockMap[v]+=1
        else:
            sockMap[v]=1

    numberOfPairs = 0
    for key in sockMap:
        v = sockMap[key]
        numberOfPairs += v//2
    return numberOfPairs

assert calcPairs([1,2,1,2,1,3,2]) == 2
assert calcPairs([10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
print("ok")