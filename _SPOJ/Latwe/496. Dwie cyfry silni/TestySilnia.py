__author__ = 'kamil'

import unittest
import math
from Silnia import liczSilnie
from Silnia import foo

class TestySilni(unittest.TestCase):
    def check(self, liczba):
        self.assertEqual(math.factorial(liczba), liczSilnie(liczba))

    def test_2(self):
        self.check(2)

    def test_3(self):
        self.check(3)

    def test_4(self):
        self.check(4)

    def test_5(self):
        self.check(5)

    def test_6(self):
        self.check(6)

class TestyZadania(unittest.TestCase):
    def test_1(self):
        self.assertEqual("0 1", foo(1))

    def test_4(self):
        self.assertEqual("2 4", foo(4))

    def test_5(self):
        self.assertEqual("2 0", foo(5))

    def test_6(self):
        self.assertEqual("2 0", foo(6))

    def test_7(self):
        self.assertEqual("4 0", foo(7))

if __name__ == '__main__':
    unittest.main()
