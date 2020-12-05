from typing import List, Optional

# given a sorted array and a number write a fun
# that counts occurences of the number in the array

# O(logn)
def sortedFreq(ar: List[int], num: int) -> int:
    left = findLeft(ar, num)
    if left is None:
        return -1
    right = findRight(ar, num)
    assert right is not None
    return right - left + 1

def findLeft(ar: List[int], num: int) -> Optional[int]:
    left = 0
    right = len(ar) - 1
    idx = None
    while left <= right:
        mid = (right +left)//2
        if ar[mid] < num:
            left = mid + 1
        else:
            right = mid -1
            if ar[mid] == num:
                idx = mid
    return idx

def findRight(ar: List[int], num: int) -> Optional[int]:
    left = 0
    right = len(ar) - 1
    idx = None
    while left <= right:
        mid = (right +left)//2
        if ar[mid] == num:
            idx = mid
        if ar[mid] > num:
           right = mid -1
        else:
            left = mid + 1
       
    return idx

assert findLeft([1,1,1,1,1,3], 1) == 0
assert findLeft([1,1,3,3,3,3], 3) == 2
assert findLeft([1,1,2,2,2,2,3], 2) == 2
assert findLeft([1,1,2,2,2,2,3], 3) == 6
assert findLeft([1,1,2,2,2,2,3], 1) == 0
assert findLeft([1,1,2,2,2,2,3], 4) is None
assert findLeft([1,1,2,2,2,2,3], 0) is None
assert findLeft([], 4) is None

assert findRight([1,1,1,1,1,3], 1) == 4
assert findRight([1,1,3,3,3,3], 3) == 5
assert findRight([1,1,2,2,2,2,3], 2) == 5
assert findRight([1,1,2,2,2,2,3], 3) == 6
assert findRight([1,1,2,2,2,2,3], 1) == 1
assert findRight([1,1,2,2,2,2,3], 4) is None
assert findRight([], 4) is None

assert sortedFreq([1,1,1,1,1,3], 1) == 5
assert sortedFreq([1,1,3,3,3,3], 3) == 4
assert sortedFreq([1,1,2,2,2,2,3], 2) == 4
assert sortedFreq([1,1,2,2,2,2,3], 3) == 1
assert sortedFreq([1,1,2,2,2,2,3], 1) == 2
assert sortedFreq([1,1,2,2,2,2,3], 4) == -1
assert sortedFreq([], 4) == -1