import unittest
from typing import List

def dutchFlag(arr: List[int], pivotIdx: int) -> List[int]:
    # like sorting quicksort product
    # less then pivot to the left, then equal, then higher to the right

    # partition to less, eq, unsolved, high
    pivotVal = arr[pivotIdx]
    loId, eqId, hiId = 0, 0, len(arr)-1
    while eqId <= hiId:
        el = arr[eqId]
        if el < pivotVal:
            arr[loId],arr[eqId] = arr[eqId],arr[loId]
            eqId += 1
            loId += 1
        elif el > pivotVal:
            arr[eqId],arr[hiId] = arr[hiId],arr[eqId]
            hiId -= 1
        else:
            eqId += 1
            
    return arr

def evenOdd(arr: List[int]) -> List[int]:
    i = 0 # these will be even
    odd_idx = len(arr)-1
    # naturally forming unsorted area in the middle
    while i < odd_idx:
        if arr[i] % 2 == 0:
            i += 1
        else:
            arr[i],arr[odd_idx] = arr[odd_idx],arr[i]
            odd_idx-=1
    return arr

class TestArrays(unittest.TestCase):

    # even elements to the beginning, odd to the end
    # O(n), space O(1)
    def testEvenOnn(self):
        data = [
            ([1,1,1,1], [1,1,1,1]),
            ([1,1,2,1], [2,1,1,1]),
            ([1,1,2,4], [4,2,1,1]),
            ([1,1,4], [4,1,1]),
            ([1,2,3,4,5,6], [6,2,4,5,3,1]),
            ([1,2,3,4,5,6,7], [6,2,4,5,3,7,1]),
        ]
        for d in data:
            with self.subTest(str(d[0])):
                self.assertEqual(d[1], evenOdd(d[0]))

    def testDutchFlag(self):
        data: List[tuple[List[int], int, List[int]]] = [
            ([0,1,2,0,2,1], 3, [0,0,2,2,1,1]),
            ([0,1,2,0,2,1], 0, [0,0,2,2,1,1]),
            ([0,1,2,0,2,1], 1, [0,0,1,1,2,2]),
            ([0,1,2,0,2,1], 2, [0,1,0,1,2,2]),
            ([1,1,1,1,1,1], 2, [1,1,1,1,1,1]),
            ([1,1,2,1,1,1], 2, [1,1,1,1,1,2]),
            ([2,1,1,1,1,1], 0, [1,1,1,1,1,2]),
            ([1,1,1,1,1,2], 5, [1,1,1,1,1,2]),
        ]
        for d in data:
            with self.subTest(f'{d[0]} {d[1]}'):
                self.assertEqual(d[2], dutchFlag(d[0], d[1]), f'id {d[1]}, el {d[0][d[1]]}')

    def testStocks(self):
        d = [310,315,275,295,260,270,290,230,255,250]
        self.assertEqual(30, stocks(d))

    def testRearrangeArray(self):
        d=[310,315,275,295,260,270,290,230,255,250]
        self.assertEqual([230, 255, 250, 270, 260, 290, 275, 310, 295, 315], rearrange(d))


# find max profit possible
# find minimum so far and return max diff from that min and already seen
def stocks(stockPrices: List[int]) -> int:
    currentMinIdx = 0
    maxDiff = 0
    for i in range(1,len(stockPrices)):
        if stockPrices[currentMinIdx] > stockPrices[i]:
            currentMinIdx = i
        
        maxDiff = max(maxDiff, stockPrices[i] - stockPrices[currentMinIdx])

    return maxDiff

# rearrange array so it has a property 
# A[0] <= A[1] >= A[2] <= A[3] >= A[4] <= ...
def rearrange(arr: List[int]) -> List[int]:
    arr.sort()
    for i in range(1,len(arr)-1,2):
        arr[i],arr[i+1] = arr[i+1], arr[i]
        
    return arr

if __name__ == '__main__':
    unittest.main()