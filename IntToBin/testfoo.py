__author__ = 'kamil'

import unittest
from foo import foo

class IntToBin(unittest.TestCase):
    def test0(self):
        self.assertEqual('0', foo(0))
    def test1(self):
        self.assertEqual('1', foo(1))
    def test2(self):
        self.assertEqual('10', foo(2))
    def test3(self):
        self.assertEqual('11', foo(3))
    def test4(self):
        self.assertEqual('100', foo(4))
    def test5(self):
        self.assertEqual('101', foo(5))
    def test6(self):
        self.assertEqual('110', foo(6))
    def test7(self):
        self.assertEqual('111', foo(7))
    def test8(self):
        self.assertEqual('1000', foo(8))
    def test9(self):
        self.assertEqual('1001', foo(9))

    def testUltimate(self):
        for i in range(100000):
            expected = bin(i).replace('0b', '')
            self.assertEqual(expected, foo(i))

if __name__ == '__main__':
    unittest.main()
