# https://www.hackerrank.com/challenges/picking-numbers/problem
from typing import List

def findLongest(tab: List[int]) -> int:
    tab.sort()

    bottomIdx = 0
    maxLen = 0
    for i in range(len(tab)-1):
        el = tab[i]
        nextEl = tab[i+1]

        if abs(el-nextEl) <= 1:
            topIdx = i+1
        else:
            bottomIdx = i + 1
            topIdx = bottomIdx

        maxLen = max(maxLen, topIdx-bottomIdx+1)
    print(f'{tab} -> {maxLen}')
    return maxLen

assert findLongest([1,1,2,2,4,4,5,5,5]) == 5
assert findLongest([4,6,5,3,3,1]) == 3
assert findLongest([1, 2, 2, 3, 1, 2]) == 5


print("all gut")