__author__ = 'kamil'

import unittest
from foo import insertionSort
import random
class testyInsertionSort(unittest.TestCase):

    def testCzyTworzyNowaTablica(self):
        tab = [4,8,6,21,5,6,7,8,2,1,0,3,9]
        self.assertNotEqual(tab, insertionSort(tab))

    def test1(self):
        tab = [5,3,68,4,43,6,7,34,25,7,3,35,76]
        self.assertEqual(sorted(tab), insertionSort(tab))

    def test2(self):
        tab = [4,8,6,21,5,6,7,8,2,1,0,3,9]
        self.assertEqual(sorted(tab), insertionSort(tab))

    def test3(self):
        tab = [5,2,4,6,1,3]
        self.assertEqual(sorted(tab), insertionSort(tab))

    def test4(self):
        tab = [5,4,8,62,4,2,6,4,7,98,5,7,5,6,2,4,1,1,4,5,3,6,5]
        self.assertEqual(sorted(tab), insertionSort(tab))

    def test5(self):
        tab = [9,8,7,6,5,4,3,2,1]
        self.assertEqual(sorted(tab), insertionSort(tab))

    def test6(self):
        tab = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(sorted(tab), insertionSort(tab))

    def stressTest(self):
        randomTab = [random.randint(0,20) for i in range(300)]
        self.assertEqual(sorted(randomTab), insertionSort(randomTab))

if __name__ == '__main__':
    unittest.main()
