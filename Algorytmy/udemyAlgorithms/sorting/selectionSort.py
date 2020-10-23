from typing import List

# compared to buble - instead of putting biggest to the end
# we place small into sorted position

# search for smallest, swap with i
# O(n^2)-in general it's the same like bubble, but here we have less amount of swaps
def selectionSort(tab: List[int]) -> List[int]:
    out: List[int] = [i for i in tab]
    for i in range(len(out)):
        minimumValueIdx = i 
        for j in range(i+1, len(out)):
            if out[j] < out[minimumValueIdx]:
                minimumValueIdx = j
        # not needed, just small optimization
        if i != minimumValueIdx:
            out[minimumValueIdx], out[i] = out[i], out[minimumValueIdx]
    return out

assert selectionSort([-4, 2, 3]) == [-4,2,3]
assert selectionSort([9, 8, -3, 3, -3]) == [-3,-3,3,8,9]
assert selectionSort([6, -3, -3, 4, -3, 3]) == [-3,-3,-3,3,4,6]
assert selectionSort([9, -1, -3, 0, 5, 2, 1]) == [-3,-1,0,1,2,5,9]
assert selectionSort([2, 5, 7, -1, 6, -1, 7, -1]) == [-1,-1,-1,2,5,6,7,7]
assert selectionSort([8, 10, 7, 3, 2, 7, -4, 6, 4]) == [-4,2,3,4,6,7,7,8,10]
assert selectionSort([9, 7, 9, 0, -3, 8, -3, 10, 9, -2]) == [-3,-3,-2,0,7,8,9,9,9,10]
assert selectionSort([i for i in range(30,-1,-1)]) == [i for i in range(31)]
