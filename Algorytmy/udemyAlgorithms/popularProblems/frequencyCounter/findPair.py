from typing import List, Dict

# given an unsorted array and a number, find if there's a pair
# whose difference is num

# solve using:
# a) space O(n), time O(n)
# b) space O(1), time O(n logn)

def findPair(ar: List[int], num: int) -> bool:
    d: Dict[int, int] = {}
    for i in ar:
        if i in d:
            d[i] += i
        else:
            d[i] = 1
    for i in ar:
        if (num+i) in d:
            return True
    return False

def binarySearch(ar: List[int], num:int) -> int:
    left = 0
    right = len(ar) -1
    while left <= right:
        mid = (right + left) // 2
        if ar[mid] == num:
            return mid
        elif num > ar[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def findPair2(ar: List[int], num: int) -> bool:
    ar.sort()
    for i in ar:
        if binarySearch(ar, num+i) != -1:
            return True
    return False

cases = [
    (([6,1,4,10,2,4], 2),True),
(([8,6,2,4,1,0,2,5,13], 1) ,True),
(([4,-2,3,10], -6) , True),
(([6,1,4,10,2,4], 22) , False),
(([], 0) , False),
(([5,5], 0) , True),
(([-4,4], -8) , True),
(([-4,4], 8) , True),
(([1,3,4,6], -2) , True),
(([0,1,3,4,6], -2), True)]

for args, res in cases:
    assert findPair(args[0], args[1]) == res

for args, res in cases:
    assert findPair2(args[0], args[1]) == res

print('ok!')