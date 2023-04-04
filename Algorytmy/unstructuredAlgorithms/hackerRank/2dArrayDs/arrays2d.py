# https://www.hackerrank.com/challenges/2d-array/problem

from typing import List

def getHourglassIdxs(id: int) -> List[int]:
    isTopRow = id < 6
    isBottomRow = id > 30
    isLeftColumn = id % 6 == 0
    isRightColumn = id % 6 == 5
    if isTopRow or isBottomRow or isLeftColumn or isRightColumn:
        return []
    return [id - 7, id - 6, id - 5, id, id + 5, id + 6, id + 7]

def sumHourglass(ids: List[int], arr: List[int]) -> int:
    suma = 0
    for i in ids:
        suma += arr[i]
    return suma

# 6x6 array, mapped as 1d array
# calc max hourglass sum
def calcHourglassSum(arr: List[int]) -> int:
    maxSum = None
    for i in range(len(arr)):
        hourglassIds = getHourglassIdxs(i)
        if len(hourglassIds) == 0:
            continue

        newSum = sumHourglass(hourglassIds, arr)
        if maxSum is None:
            maxSum = newSum
        else:
            maxSum = max(maxSum, newSum)

    return maxSum

assert getHourglassIdxs(0) == []
assert getHourglassIdxs(1) == []
assert getHourglassIdxs(5) == []
assert getHourglassIdxs(6) == []
assert getHourglassIdxs(7) == [0,1,2,7,12,13,14]
assert getHourglassIdxs(9) == [2,3,4,9,14,15,16]
assert getHourglassIdxs(11) == []
assert getHourglassIdxs(12) == []

assert calcHourglassSum([-9,-9,-9, 1,1,1,
 0,-9, 0, 4,3,2,
-9,-9,-9, 1,2,3,
 0, 0, 8, 6,6,0,
 0, 0, 0,-2,0,0,
 0, 0, 1, 2,4,0]) == 28

assert calcHourglassSum([1,1,1,0,0,0,
0,1,0,0,0,0,
1,1,1,0,0,0,
0,0,2,4,4,0,
0,0,0,2,0,0,
0,0,1,2,4,0]) == 19


print('arrays ok')