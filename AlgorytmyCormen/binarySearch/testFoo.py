__author__ = 'kamil'

import unittest
from foo import binSearch
from foo import binSearchX

class testySzukaniaBinarnego(unittest.TestCase):
    def test0(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearch(tab, 2))

    def test1(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearch(tab, 4))

    def test2(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearch(tab, 3))

    def test3(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearch(tab, 5))

    def test4(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearch(tab, 1))

    def test5(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(False, binSearch(tab, -1))

    def test6(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(False, binSearch(tab, 0))

    def test7(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(True, binSearch(tab, 4))

    def test8(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(True, binSearch(tab, 3))

    def test9(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(True, binSearch(tab, 5))

    def test10(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(True, binSearch(tab, 1))

    def test11(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(False, binSearch(tab, 8))

    def test12(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(False, binSearch(tab, 0))

class testySzukaniaBinarnegoIteracyjnie(unittest.TestCase):
    def test0(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearchX(tab, 2))

    def test1(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearchX(tab, 4))

    def test2(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearchX(tab, 3))

    def test3(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearchX(tab, 5))

    def test4(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(True, binSearchX(tab, 1))

    def test5(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(False, binSearchX(tab, -1))

    def test6(self):
        tab=[1,2,3,4,5,6,7,8]
        self.assertEqual(False, binSearchX(tab, 0))

    def test7(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(True, binSearchX(tab, 4))

    def test8(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(True, binSearchX(tab, 3))

    def test9(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(True, binSearchX(tab, 5))

    def test10(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(True, binSearchX(tab, 1))

    def test11(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(False, binSearchX(tab, 8))

    def test12(self):
        tab=[1,2,3,4,5,6,7]
        self.assertEqual(False, binSearchX(tab, 0))


if __name__ == '__main__':
    unittest.main()
