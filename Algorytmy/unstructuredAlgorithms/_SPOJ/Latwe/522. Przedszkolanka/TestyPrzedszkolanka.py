__author__ = 'kamil'

import unittest
from Przedszkolanka import foo
from Przedszkolanka import nwd

class TestyPrzedszkolanki(unittest.TestCase):
    def test_1(self):
        self.assertEqual(60, foo(12, 15))
    def test_2(self):
        self.assertEqual(22, foo(11, 22))

class Nwd(unittest.TestCase):
    def test_42_56(self):
        self.assertEqual(14, nwd(42,56))

    def test_36_48(self):
        self.assertEqual(12, nwd(36,48))

    def test_8_12(self):
        self.assertEqual(4, nwd(8,12))

    def test_9_28(self):
        self.assertEqual(1, nwd(9,28))

if __name__ == '__main__':
    unittest.main()
