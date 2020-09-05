import unittest
from typing import List
from binarySearch import BinarySearch
import logging

class TestFoo(unittest.TestCase):
    def getEvenArray(self) -> List[int]:
        return [0,1,2,3,4,5,6, 8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

    def getOddArray(self) -> List[int]:
        return [0,1,2,3,4,5,6, 8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    def testPresent(self):
        bs = BinarySearch(self.getEvenArray())
        self.assertEqual(9, bs.binarySearch(10))
        self.assertEqual(21, bs.binarySearch(22))
        self.assertEqual(0, bs.binarySearch(0))
        self.assertEqual(23, bs.binarySearch(24))

    def testNotPresent(self):
        bs = BinarySearch(self.getEvenArray())
        self.assertEqual(-1, bs.binarySearch(-20))
        self.assertEqual(-1, bs.binarySearch(7))
        self.assertEqual(-1, bs.binarySearch(25))
        
    def testPresent2(self):
        bs = BinarySearch(self.getOddArray())
        self.assertEqual(9, bs.binarySearch(10))
        self.assertEqual(21, bs.binarySearch(22))
        self.assertEqual(0, bs.binarySearch(0))

    def testNotPresent2(self):
        bs = BinarySearch(self.getOddArray())
        self.assertEqual(-1, bs.binarySearch(-20))
        self.assertEqual(-1, bs.binarySearch(7))
        self.assertEqual(-1, bs.binarySearch(24))

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    unittest.main()