import unittest
from typing import List

# In a particular board garne, a player has to try to advance through a sequence of positions. Each
# position has a nonnegative integer associated with it, representing the maximum you can advance
# from that position in one move. You begin at the first position, and win by getting to the last
# position

# Write a program which takes an array of n integers, where A[i] denotes the maximum you can
# advance from index i, and returns whether it is possible to advance to the last index starting from
# the beginning of the array
class TestMoves(unittest.TestCase):
    def testMove1(self):
        self.assertTrue(move([3,3,1,0,2,0,1]))
    
    def testMove2(self):
        self.assertTrue(move([2,4,1,1,0,2,3]))

    def testMove3(self):
        self.assertFalse(move([3,2,0,0,2,0,1]))

def move(arr: List[int]) -> bool:
    farthest = 0
    for i in range(len(arr)):
        if i <= farthest:
            farthest = max(farthest, i + arr[i])
        
    return farthest >= len(arr)-1

if __name__ == '__main__':
    unittest.main()