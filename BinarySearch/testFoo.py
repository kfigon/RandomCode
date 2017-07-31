__author__ = 'kamil'

import unittest
from foo import foo

class testBinarySearch(unittest.TestCase):
    def test1(self):
        tab=[1,2,3,4,5,6,7,8,9]
        self.assertEqual(True, foo(tab, 2))

    def test2(self):
        tab=[1,2,3,4,5,6,7,8,9]
        self.assertEqual(True, foo(tab, 1))

    def test3(self):
        tab=[1,2,3,4,5,6,7,8,9]
        self.assertEqual(True, foo(tab, 8))

    def test4(self):
        tab=[1,2,3,4,5,6,7,8,9]
        self.assertEqual(False, foo(tab, 11))

    def test5(self):
        tab=[1,2,3,4,5,6,7,8,9]
        self.assertEqual(False, foo(tab, -3))

    def test6(self):
        tab=[1,2,3,4,5,6,7,8,9, 10]
        self.assertEqual(False, foo(tab, -3))

    def test7(self):
        tab=[1,2,3,4,5,6,7,8,9, 10]
        self.assertEqual(True, foo(tab, 5))

    def test8(self):
        tab=[1,2,3,4,5,6,7,8,9, 10]
        self.assertEqual(True, foo(tab, 1))


if __name__ == '__main__':
    unittest.main()
