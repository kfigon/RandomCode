__author__ = 'kamil'

import unittest
from FloatPrinter import foo

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("0x3f 0x80 0x0 0x0", foo(1))

    def test_minus1(self):
        self.assertEqual("0xbf 0x80 0x0 0x0", foo(-1))

    def test_0(self):
        self.assertEqual("0x0 0x0 0x0 0x0", foo(0))

    def test_123_125(self):
        self.assertEqual("0x42 0xf6 0x40 0x0", foo(123.125))

    def test_minus345(self):
        self.assertEqual("0xc3 0xac 0x80 0x0", foo(-345))

    def test_minus3456_23(self):
        self.assertEqual("0xc5 0x58 0x3 0xae", foo(-3456.23))

    def test_minus929493_34(self):
        self.assertEqual("0xc9 0x62 0xed 0x55", foo(-929493.34))

if __name__ == '__main__':
    unittest.main()
