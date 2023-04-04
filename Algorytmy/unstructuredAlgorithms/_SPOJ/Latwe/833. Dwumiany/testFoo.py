__author__ = 'kamil'

import unittest
import math
from foo import foo
from foo import silnia

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, foo(0, 0))

    def test_2(self):
         self.assertEqual(35, foo(7, 3))

    def test_silnia_1(self):
        self.assertEqual(math.factorial(1), silnia(1))

    def test_silnia_2(self):
        self.assertEqual(math.factorial(2), silnia(2))

    def test_silnia_3(self):
        self.assertEqual(math.factorial(3), silnia(3))

    def test_silnia_4(self):
        self.assertEqual(math.factorial(4), silnia(4))

    def test_silnia_5(self):
        self.assertEqual(math.factorial(5), silnia(5))

if __name__ == '__main__':
    unittest.main()
