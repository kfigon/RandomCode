import unittest
from typing import List

def dutchFlag(arr: List[int], pivotIdx: int) -> List[int]:
    return arr

def evenOdd(arr: List[int]) -> List[int]:
    i = 0 # these will be even
    odd_idx = len(arr)-1
    # naturally forming unsorted area in the middle
    while i < odd_idx:
        el = arr[i]
        even = el % 2 == 0
        if even:
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
        self.fail('todo')
        data: List[tuple[List[int], int, List[int]]] = [
            ([], 0, []),
        ]
        for d in data:
            with self.subTest(f'{d[0]} {d[1]}'):
                self.assertEqual(d[2], dutchFlag(d[0], d[1]))

if __name__ == '__main__':
    unittest.main()