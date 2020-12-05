from typing import List, Optional

# given an array of 1s and 0s which has all 1s followed
# by all 0s, write a function which returns the number of zeroes

# O(logn)
def bruteForceCountZeroes(ar: List[int]) -> int:
    lastIIdx = 0
    while lastIIdx < len(ar) and ar[lastIIdx] == 1:
        lastIIdx += 1
    return len(ar) - lastIIdx

def findLastOneIdx(ar: List[int]) -> Optional[int]:
    left = 0
    right = len(ar)-1
    lastIIdx = None
    while left <=  right:
        mid = (right + left)//2
        if ar[mid] == 0:
            right = mid - 1
        else:
            left = mid+1
            lastIIdx = mid
    # print(f'{ar} -> {lastIIdx}')
    return lastIIdx

def countZeroes(ar: List[int]) -> int:
    lastIIdx = findLastOneIdx(ar)
    return len(ar) if (lastIIdx is None) else len(ar) - lastIIdx -1

assert findLastOneIdx([1,1,0,0]) == 1
assert findLastOneIdx([1,1,1,0]) == 2
assert findLastOneIdx([1,1,1,0,0]) == 2
assert findLastOneIdx([1,1,0,0,0]) == 1
assert findLastOneIdx([1,1,1,1,0,0]) == 3
assert findLastOneIdx([1,0,0,0,0]) == 0
assert findLastOneIdx([0,0,0]) is None
assert findLastOneIdx([1,1,1,1]) == 3

assert bruteForceCountZeroes([1,1,1,1,0,0]) == 2
assert bruteForceCountZeroes([1,0,0,0,0]) == 4
assert bruteForceCountZeroes([0,0,0]) == 3
assert bruteForceCountZeroes([1,1,1,1]) == 0

assert countZeroes([1,1,1,1,0,0]) == 2
assert countZeroes([1,0,0,0,0]) == 4
assert countZeroes([0,0,0]) == 3
assert countZeroes([1,1,1,1]) == 0

print('done')