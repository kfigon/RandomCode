from typing import List ,Tuple

# assume that we always start on 0
def moveLesserToLeft(tab: List[int]) -> Tuple[List[int], int]:
    pivotIdx: int = 0
    pivotToMove = pivotIdx + 1
    for i in range(pivotToMove, len(tab)):
        if tab[i] < tab[pivotIdx]:
            if pivotToMove != i:
                # print('swap')
                tab[i],tab[pivotToMove] = tab[pivotToMove], tab[i]
            pivotToMove += 1

    tab[pivotToMove-1],tab[pivotIdx] = tab[pivotIdx], tab[pivotToMove-1]
    return tab, pivotToMove-1

# find pivot point - any, can be first
# presort by moving lesser than pivot to left, greater to right
# then pivot is in the right place
# repeat on new left and right subarray
# 1 element arrays are sorted

# there are consequences which pivot point to choose 

# this can be optimized by using indexes instead of array slice
# overall algorithm - O(nlogn) 
# worst (already sorted and pivot is minimum or maximum) - O(n^2)
# pivot can be middle or even random
def quickSort(tab: List[int]) -> List[int]:
    if len(tab) <= 1:
        return tab
    _,pivotIdx = moveLesserToLeft(tab)
    left = tab[:pivotIdx]
    # right = tab[pivotIdx+1:] if (pivotIdx+1) < len(tab) else [] 
    right = tab[pivotIdx+1:]
    return quickSort(left) + [tab[pivotIdx]] + quickSort(right)

assert moveLesserToLeft([5,2,1,8,4,7,6,3]) == ([3,2,1,4,5,7,6,8], 4)
assert moveLesserToLeft([5,2,1,8,4,7,6]) == ([4,2,1,5,8,7,6], 3)

assert quickSort([8,3,5,4,7,6,1,2]) == [1,2,3,4,5,6,7,8]
assert quickSort([5,3,4,2,6,1]) == [1,2,3,4,5,6]
assert quickSort([i for i in range(20)]) == [i for i in range(20)]
assert quickSort([-4, 2, 3]) == [-4,2,3]
assert quickSort([9, 8, -3, 3, -3]) == [-3,-3,3,8,9]
assert quickSort([6, -3, -3, 4, -3, 3]) == [-3,-3,-3,3,4,6]
assert quickSort([9, -1, -3, 0, 5, 2, 1]) == [-3,-1,0,1,2,5,9]
assert quickSort([2, 5, 7, -1, 6, -1, 7, -1]) == [-1,-1,-1,2,5,6,7,7]
assert quickSort([8, 10, 7, 3, 2, 7, -4, 6, 4]) == [-4,2,3,4,6,7,7,8,10]
assert quickSort([9, 7, 9, 0, -3, 8, -3, 10, 9, -2]) == [-3,-3,-2,0,7,8,9,9,9,10]
assert quickSort([i for i in range(30,-1,-1)]) == [i for i in range(31)]
# stack overflow - need to switch to indexes instead of using arary slices
# assert quickSort([i for i in range(10000,-1,-1)]) == [i for i in range(10001)]
print('quicksort ok')