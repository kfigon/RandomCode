from typing import List

# split arrays to halves, until one element - this is sorted
# then merge

# O(n+m)
def merge(a: List[int], b: List[int]) -> List[int]:
    out: List[int] = []
    aIdx = 0
    bIdx = 0
    while aIdx < len(a) or bIdx < len(b):
        if aIdx >= len(a):
            out += b[bIdx:]
            bIdx = len(b)
        elif bIdx >= len(b):
            out += a[aIdx:]
            aIdx = len(a)
        elif a[aIdx] < b[bIdx]:
            out.append(a[aIdx])
            aIdx += 1
        else:
            out.append(b[bIdx])
            bIdx += 1
    return out

# O(logn)
# overall algorithm - O(nlogn)
def mergeSort(tab: List[int]) -> List[int]:
    if len(tab) <= 1:
        return tab
    splitPoint = len(tab)//2
    left = tab[:splitPoint]
    right = tab[splitPoint:]

    return merge(mergeSort(left), mergeSort(right))

assert merge([],[8]) == [8]
assert merge([8],[]) == [8]
assert merge([3],[8]) == [3,8]
assert merge([1,2],[3,4]) == [1,2,3,4]
assert merge([1,3],[2,4]) == [1,2,3,4]
assert merge([1,4],[2,3]) == [1,2,3,4]
assert merge([1],[2,3]) == [1,2,3]
assert merge([4],[2,3]) == [2,3,4]
assert merge([1,3],[2]) == [1,2,3]
assert merge([1,3],[4]) == [1,3,4]

assert mergeSort([8,3,5,4,7,6,1,2]) == [1,2,3,4,5,6,7,8]
assert mergeSort([5,3,4,2,6,1]) == [1,2,3,4,5,6]
assert mergeSort([i for i in range(20)]) == [i for i in range(20)]
assert mergeSort([-4, 2, 3]) == [-4,2,3]
assert mergeSort([9, 8, -3, 3, -3]) == [-3,-3,3,8,9]
assert mergeSort([6, -3, -3, 4, -3, 3]) == [-3,-3,-3,3,4,6]
assert mergeSort([9, -1, -3, 0, 5, 2, 1]) == [-3,-1,0,1,2,5,9]
assert mergeSort([2, 5, 7, -1, 6, -1, 7, -1]) == [-1,-1,-1,2,5,6,7,7]
assert mergeSort([8, 10, 7, 3, 2, 7, -4, 6, 4]) == [-4,2,3,4,6,7,7,8,10]
assert mergeSort([9, 7, 9, 0, -3, 8, -3, 10, 9, -2]) == [-3,-3,-2,0,7,8,9,9,9,10]
assert mergeSort([i for i in range(30,-1,-1)]) == [i for i in range(31)]
assert mergeSort([i for i in range(100000,-1,-1)]) == [i for i in range(100001)]
print('merge ok')