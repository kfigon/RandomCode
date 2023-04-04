# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
from typing import List


def leftRotateArray(arr: List[int], num: int) -> List[int]:
    rotationIdx = 0
    if num != 0:
        rotationIdx = num % len(arr)
    if rotationIdx == 0:
        return arr

    rotated: List[int] = []
    for i in range(len(arr)-rotationIdx):
        rotated.append(arr[i+rotationIdx])
    for i in range(rotationIdx):
        rotated.append(arr[i])

    print(f'{arr}, {num} -> {rotated}')
    return rotated

assert leftRotateArray([1,2,3,4,5], 0) == [1,2,3,4,5]
assert leftRotateArray([1,2,3,4,5], 1) == [2,3,4,5,1]
assert leftRotateArray([1,2,3,4,5], 2) == [3,4,5,1,2]
assert leftRotateArray([1,2,3,4,5], 4) == [5,1,2,3,4]
assert leftRotateArray([1,2,3,4,5], 5) == [1,2,3,4,5]
assert leftRotateArray([1,2,3,4,5], 6) == [2,3,4,5,1]
print('ok!')