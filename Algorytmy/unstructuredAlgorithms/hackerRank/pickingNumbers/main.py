# https://www.hackerrank.com/challenges/picking-numbers/problem
from typing import List

def findLongest(tab: List[int]) -> int:
    tab.sort()

    bottomIdx = 0
    maxLen = 0
    minEl = tab[0]
    for i in range(1,len(tab)):
        el = tab[i]

        if abs(minEl-el) <= 1:
            maxLen = max(maxLen, i - bottomIdx + 1)
        else:
            bottomIdx = i
            minEl = tab[i]

    print(f'{tab} -> {maxLen}')
    return maxLen

assert findLongest([1,1,2,2,4,4,5,5,5]) == 5
assert findLongest([4,6,5,3,3,1]) == 3 # 1 3 3 4 5 6
assert findLongest([1, 2, 2, 3, 1, 2]) == 5


print("all gut")