from typing import List

# O(n^2)
# najwiekszy babelek wyplywa na gore
# w kazdej iteracji
def bubbleSort(tab: List[int]) -> List[int]:
    out: List[int] = [i for i in tab]
    sortedElements = 0
    while sortedElements < len(out):
        i = 0
        j = i + 1
        while j < (len(out) - sortedElements):
            if out[i] > out[j]:
                out[i],out[j] = out[j],out[i]
            i += 1
            j += 1
        sortedElements += 1
    return out

# czytelniejsza implementacja:
def bubbleSort2(tab: List[int]) -> List[int]:
    out: List[int] = [i for i in tab]
        
    for i in range(len(out)-1, -1, -1):
        for j in range(0, i):
            if out[j] > out[j+1]:
                out[j],out[j+1] = out[j+1],out[j]
    return out

# on presorted
# even O(n) when good case
def bubbleSortOptimized(tab: List[int]) -> List[int]:
    out: List[int] = [i for i in tab]
    for i in range(len(out)-1, -1, -1):
        noSwaps = True
        for j in range(0, i):
            if out[j] > out[j+1]:
                out[j],out[j+1] = out[j+1], out[j]
                noSwaps = False
        if noSwaps:
            break
    return out


assert bubbleSort([-4, 2, 3]) == [-4,2,3]
assert bubbleSort([9, 8, -3, 3, -3]) == [-3,-3,3,8,9]
assert bubbleSort([6, -3, -3, 4, -3, 3]) == [-3,-3,-3,3,4,6]
assert bubbleSort([9, -1, -3, 0, 5, 2, 1]) == [-3,-1,0,1,2,5,9]
assert bubbleSort([2, 5, 7, -1, 6, -1, 7, -1]) == [-1,-1,-1,2,5,6,7,7]
assert bubbleSort([8, 10, 7, 3, 2, 7, -4, 6, 4]) == [-4,2,3,4,6,7,7,8,10]
assert bubbleSort([9, 7, 9, 0, -3, 8, -3, 10, 9, -2]) == [-3,-3,-2,0,7,8,9,9,9,10]
assert bubbleSort([i for i in range(30,-1,-1)]) == [i for i in range(31)]

assert bubbleSort2([-4, 2, 3]) == [-4,2,3]
assert bubbleSort2([9, 8, -3, 3, -3]) == [-3,-3,3,8,9]
assert bubbleSort2([6, -3, -3, 4, -3, 3]) == [-3,-3,-3,3,4,6]
assert bubbleSort2([9, -1, -3, 0, 5, 2, 1]) == [-3,-1,0,1,2,5,9]
assert bubbleSort2([2, 5, 7, -1, 6, -1, 7, -1]) == [-1,-1,-1,2,5,6,7,7]
assert bubbleSort2([8, 10, 7, 3, 2, 7, -4, 6, 4]) == [-4,2,3,4,6,7,7,8,10]
assert bubbleSort2([9, 7, 9, 0, -3, 8, -3, 10, 9, -2]) == [-3,-3,-2,0,7,8,9,9,9,10]
assert bubbleSort2([i for i in range(30,-1,-1)]) == [i for i in range(31)]

assert bubbleSortOptimized([-4, 2, 3]) == [-4,2,3]
assert bubbleSortOptimized([9, 8, -3, 3, -3]) == [-3,-3,3,8,9]
assert bubbleSortOptimized([6, -3, -3, 4, -3, 3]) == [-3,-3,-3,3,4,6]
assert bubbleSortOptimized([9, -1, -3, 0, 5, 2, 1]) == [-3,-1,0,1,2,5,9]
assert bubbleSortOptimized([2, 5, 7, -1, 6, -1, 7, -1]) == [-1,-1,-1,2,5,6,7,7]
assert bubbleSortOptimized([8, 10, 7, 3, 2, 7, -4, 6, 4]) == [-4,2,3,4,6,7,7,8,10]
assert bubbleSortOptimized([9, 7, 9, 0, -3, 8, -3, 10, 9, -2]) == [-3,-3,-2,0,7,8,9,9,9,10]
assert bubbleSortOptimized([i for i in range(30,-1,-1)]) == [i for i in range(31)]