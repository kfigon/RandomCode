from typing import List

# we're making sorted portion of array <0;i)
# it's good when it's presorted
# and when we're streaming data - one part of array is already sorted
# O(n^2)
def insertionSort(tab: List[int]) -> List[int]:
    out: List[int] = [i for i in tab]
    for i in range(1,len(out)):
        j = i-1
        currElement = out[i]
        while j >= 0 and currElement < out[j]:
            out[j+1] = out[j]
            j -= 1
        out[j+1] = currElement
    return out

assert insertionSort([5,3,4,2,4,6,1]) == [1,2,3,4,4,5,6]
assert insertionSort([-4, 2, 3]) == [-4,2,3]
assert insertionSort([9, 8, -3, 3, -3]) == [-3,-3,3,8,9]
assert insertionSort([6, -3, -3, 4, -3, 3]) == [-3,-3,-3,3,4,6]
assert insertionSort([9, -1, -3, 0, 5, 2, 1]) == [-3,-1,0,1,2,5,9]
assert insertionSort([2, 5, 7, -1, 6, -1, 7, -1]) == [-1,-1,-1,2,5,6,7,7]
assert insertionSort([8, 10, 7, 3, 2, 7, -4, 6, 4]) == [-4,2,3,4,6,7,7,8,10]
assert insertionSort([9, 7, 9, 0, -3, 8, -3, 10, 9, -2]) == [-3,-3,-2,0,7,8,9,9,9,10]
assert insertionSort([i for i in range(30,-1,-1)]) == [i for i in range(31)]
