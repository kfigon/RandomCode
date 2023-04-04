__author__ = 'kamil'

import unittest
from LiczbyPierwsze import fun
from LiczbyPierwsze import fun2

class bruteForce(unittest.TestCase):
    def test_11(self):
        self.assertEqual("TAK", fun(11))

    def test_1(self):
        self.assertEqual("NIE", fun(1))

    def test_4(self):
        self.assertEqual("NIE", fun(4))

    def test_2(self):
        self.assertEqual("TAK", fun(2))

    def test_3(self):
        self.assertEqual("TAK", fun(3))

    def test_5(self):
        self.assertEqual("TAK", fun(5))

    def test_6(self):
        self.assertEqual("NIE", fun(6))

    def test_7(self):
        self.assertEqual("TAK", fun(7))

    def test_8(self):
        self.assertEqual("NIE", fun(8))

    def test_56(self):
        self.assertEqual("NIE", fun(56))

    def test_103(self):
        self.assertEqual("TAK", fun(103))

    def test_7919(self):
        self.assertEqual("TAK", fun(7919))

class sito(unittest.TestCase):
    def test_11(self):
        self.assertEqual("TAK", fun2(11))

    def test_1(self):
        self.assertEqual("NIE", fun2(1))

    def test_4(self):
        self.assertEqual("NIE", fun2(4))

    def test_2(self):
        self.assertEqual("TAK", fun2(2))

    def test_3(self):
        self.assertEqual("TAK", fun2(3))

    def test_5(self):
        self.assertEqual("TAK", fun2(5))

    def test_6(self):
        self.assertEqual("NIE", fun2(6))

    def test_7(self):
        self.assertEqual("TAK", fun2(7))

    def test_8(self):
        self.assertEqual("NIE", fun2(8))

    def test_56(self):
        self.assertEqual("NIE", fun2(56))

    def test_103(self):
        self.assertEqual("TAK", fun2(103))

    def test_7919(self):
        self.assertEqual("TAK", fun2(7919))

if __name__ == '__main__':
    unittest.main()
