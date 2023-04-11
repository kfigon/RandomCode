import unittest
from typing import List

def dutchFlag(arr: List[int], pivotIdx: int) -> List[int]:
    return arr

def evenOdd(arr: List[int]) -> List[int]:
    even_idx = 0
    odd_idx = len(arr)-1
    i = 0
    while i < len(arr):
        el = arr[i]
        even = el % 2 == 0
        if even:
            arr[even_idx],arr[i] = arr[i],arr[even_idx]
            even_idx+=1
        else:
            arr[odd_idx],arr[i] = arr[i],arr[odd_idx]
            odd_idx-=1
        i+=1
    return arr

class TestArrays(unittest.TestCase):

    # even elements to the beginning, odd to the end
    # O(n), space O(1)
    def testEvenOnn(self):
        data = [
            ([1,1,1,1], [1,1,1,1]),
            ([1,1,2,1], [2,1,1,1]),
            ([1,1,2,4], [2,4,1,1]),
            ([1,1,4], [4,1,1]),
            ([1,2,3,4,5,6], [2,4,6,1,3,5]),
            ([1,2,3,4,5,6,7], [2,4,6,1,3,5,7]),
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