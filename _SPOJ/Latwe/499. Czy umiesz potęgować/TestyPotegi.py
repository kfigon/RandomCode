__author__ = 'kamil'

import unittest
from Potegi import foo

class TestyPotegi(unittest.TestCase):
    def test_1(self):
        self.assertEqual("8", foo(2,3))

    def test_2(self):
        self.assertEqual("7", foo(3,3))

    def test_3(self):
        self.assertEqual("6", foo(4,4))

    def test_4(self):
        self.assertEqual("1", foo(3,4))

    def test_5(self):
        self.assertEqual("5", foo(5,1))

    def test_6(self):
        self.assertEqual("1", foo(1,8))

if __name__ == '__main__':
    unittest.main()
