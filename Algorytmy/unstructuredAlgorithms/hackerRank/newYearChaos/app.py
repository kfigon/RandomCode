# https://www.hackerrank.com/challenges/new-year-chaos/problem
from typing import List


def checkQueue(arr: List[int]) -> int:
    pendingScore = 0
    for i,v in enumerate(arr):
        shouldBe = v-1
        if shouldBe-i > 2:
            return -1
        for j in range(max(shouldBe-1, 0), i): # idk why this works :(
            if arr[j] > shouldBe:
                pendingScore += 1

    return pendingScore

assert checkQueue([1,2,3,5,4,6,7,8]) == 1
assert checkQueue([2,1,5,3,4]) == 3
assert checkQueue([1,2,5,3,7,8,6,4]) == 7

assert checkQueue([2,5,1,3,4]) == -1
assert checkQueue([4,1,2,3]) == -1
assert checkQueue([5,1,2,3,7,8,6,4]) == -1

print('olk')
