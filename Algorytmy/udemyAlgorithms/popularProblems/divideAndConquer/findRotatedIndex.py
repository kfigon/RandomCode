from typing import List

# fun that accepts a rotated array of sorted numbers and an int
# fun should return the index of the integer in the array or -1

# time O(logn)
# space O(1)

def findPivot(ar: List[int]) -> int:
    left = 0
    right = len(ar) - 1
    while left <= right and (left+1 != right):
        mid = (right+left) // 2
        if ar[mid] < ar[left]:
            right = mid
        else:
            left = mid
    # corner case - already sorted
    if right == len(ar) -1:
        return 0
    return right

def binarySearch(ar: List[int], num: int, initLeft, initRight) -> int:
    left = initLeft
    right = initRight
    while left <= right:
        mid = (right+left)//2
        if ar[mid] == num:
            return mid
        elif num < ar[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def findRotatedIdx(ar: List[int], num: int) -> int:
    pivot = findPivot(ar)
    if pivot == 0:
        return binarySearch(ar, num, 0, len(ar)-1)
    
    resultInLeft = binarySearch(ar, num, 0, pivot-1)
    if resultInLeft != -1:
        return resultInLeft
    
    return binarySearch(ar, num, pivot, len(ar)-1)


assert findPivot([3,4,1,2]) == 2
assert findPivot([3,4,1,2,3]) == 2
assert findPivot([3,4,5,1,2]) == 3
assert findPivot([1,2,3,4]) == 0
assert findPivot([6,7,8,9,1,2,3,4]) == 4
assert findPivot([37,44,66,102,10,22]) == 4
assert findPivot([11,12,13,14,15,16,3,5,7,9]) == 6
assert findPivot([7,3,4,5,6]) == 1
assert findPivot([7,3,4,5]) == 1

assert findRotatedIdx([3,4,1,2], 4) == 1
assert findRotatedIdx([6,7,8,9,1,2,3,4], 8) == 2
assert findRotatedIdx([6,7,8,9,1,2,3,4], 3) == 6
assert findRotatedIdx([37,44,66,102,10,22], 14) == -1
assert findRotatedIdx([6,7,8,9,1,2,3,4], 12) == -1
assert findRotatedIdx([11,12,13,14,15,16,3,5,7,9], 16) == 5
assert findRotatedIdx([1,2,3,4,5,6,7,8,9], 1) == 0
assert findRotatedIdx([1,2,3,4,5,6,7,8,9], 8) == 7

print('ok!')