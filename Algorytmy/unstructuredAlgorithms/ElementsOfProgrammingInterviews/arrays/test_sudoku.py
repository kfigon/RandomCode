import unittest
from typing import List

input1 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0], 
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0] ]

input2 = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6], 
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9] ]


def check(x: List[int]) -> bool:
    block = list(filter(lambda el: el != 0, x))
    return len(block) == len(set(block))

def checker(arr: List[List[int]]) -> bool:
    for i in range(9):
        if not check(rows(arr,i)) or not check(cols(arr,i)) or not check(square(arr, i)):
            return False
    return True

def rows(arr: List[List[int]], idx: int) -> List[int]:
    return [arr[idx][c] for c in range(len(arr[idx]))]

def cols(arr: List[List[int]], idx: int) -> List[int]:
    return [arr[r][idx] for r in range(len(arr))]

def square(arr: List[List[int]], idx: int) -> List[int]:
    d = [
        ([0,1,2], [0,1,2]), ([0,1,2], [3,4,5]), ([0,1,2], [6,7,8]), 
        ([3,4,5], [0,1,2]), ([3,4,5], [3,4,5]), ([3,4,5], [6,7,8]), 
        ([6,7,8], [0,1,2]), ([6,7,8], [3,4,5]), ([6,7,8], [6,7,8]), 
    ]
    rows,cols = d[idx]
    out = []
    for r in rows:
        for c in cols:
            out.append(arr[r][c])
    return out

# check if there're no duplicates in row, column and square
# in partially solved sudoku
class TestSudoku(unittest.TestCase):
    def testChecker(self):
        self.assertTrue(checker(input1))
    def testChecker2(self):
        self.assertTrue(checker(input2))

if __name__ == '__main__':
    unittest.main()