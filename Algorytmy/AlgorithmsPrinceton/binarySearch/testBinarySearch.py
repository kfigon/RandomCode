import unittest
import random
from typing import List
from binarySearch import BinarySearch, Przedzial
import logging

class TestFoo(unittest.TestCase):
    def getEvenArray(self) -> List[int]:
        return [0,1,2,3,4,5,6, 8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

    def getOddArray(self) -> List[int]:
        return [0,1,2,3,4,5,6, 8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    def testEvenPresent(self):
        kejsy = [
            (9,10),
            (21,22),
            (0,0),
            (23,24)
        ]
        bs: BinarySearch = BinarySearch(self.getEvenArray())
        for k in kejsy:
            with self.subTest(k):
                self.assertEqual(k[0], bs.binarySearch(k[1]))        

    def testEvenNotPresent(self):
        kejsy = [-20, 7, 25]
        bs: BinarySearch = BinarySearch(self.getEvenArray())
        for k in kejsy:
            with self.subTest(k):
                self.assertEqual(-1, bs.binarySearch(k))
        
    def testOddPresent(self):
        kejsy = [
            (9,10),
            (21,22),
            (0,0)
        ]
        bs: BinarySearch = BinarySearch(self.getOddArray())
        for k in kejsy:
            with self.subTest(k):
                self.assertEqual(k[0], bs.binarySearch(k[1]))  

    def testOddNotPresent(self):
        kejsy = [-20, 7, 24]
        bs: BinarySearch = BinarySearch(self.getOddArray())
        for k in kejsy:
            with self.subTest(k):
                self.assertEqual(-1, bs.binarySearch(k))  

    def testStress(self):
        sizes = [4,5,6,7,8,20,21,22,23,30,31]
        for size in sizes:
            for _ in range(100):
                ar = [random.randint(-5, 20) for _ in range(size)]
                ar.sort()
                bs = BinarySearch(ar)
                randomElement = ar[random.randint(0, len(ar)-1)]
                foundId = bs.binarySearch(randomElement)
                self.assertEqual(randomElement, ar[foundId])

class TestyPrzedzialu(unittest.TestCase):
    def testMiddle(self):
        self.assertEqual(2, Przedzial(0, 5).getMiddleIdx())
        self.assertEqual(3, Przedzial(0, 6).getMiddleIdx())
        self.assertEqual(5, Przedzial(5, 6).getMiddleIdx())
        self.assertEqual(5, Przedzial(5, 6).getMiddleIdx())
        self.assertEqual(5, Przedzial(5, 5).getMiddleIdx())

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    # logging.basicConfig(level=logging.INFO)

    unittest.main()
