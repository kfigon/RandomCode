import unittest
from typing import List

def dutchFlag(arr: List[int], pivotIdx: int) -> List[int]:
    # like sorting quicksort product
    # less then pivot to the left, then equal, then higher to the right
    pivotVal = arr[pivotIdx]
    loId, eqId, hiId = 0, 0, len(arr)
    while eqId < hiId:
        el = arr[eqId]
        if el < pivotVal:
            arr[loId],arr[eqId] = arr[eqId],arr[loId]
            eqId += 1
            loId += 1
        elif el > pivotVal:
            hiId -= 1
            arr[eqId],arr[hiId] = arr[hiId],arr[eqId]
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

if __name__ == '__main__':
    unittest.main()