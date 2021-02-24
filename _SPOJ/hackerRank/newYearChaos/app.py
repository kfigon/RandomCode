# https://www.hackerrank.com/challenges/new-year-chaos/problem
from typing import List


def checkQueue(arr: List[int]) -> int:
    pendingScore = 0
    for i,v in enumerate(arr):
        shouldBe = v-1
        dif = shouldBe - i
        if dif > 2:
            return -1
        elif dif > 0:
            pendingScore += dif
    print(f'{arr} -> {pendingScore}')
    return pendingScore

assert checkQueue([1,2,3,5,4,6,7,8]) == 1
assert checkQueue([2,1,5,3,4]) == 3
assert checkQueue([1,2,5,3,7,8,6,4]) == 7 # 6 is not counted
                 # 0 1 2 3 4 5 6 7
                 # 0 1 4 2 6 7 5 3    should be idx
assert checkQueue([2,5,1,3,4]) == -1
assert checkQueue([4,1,2,3]) == -1
assert checkQueue([5,1,2,3,7,8,6,4]) == -1

print('olk')
