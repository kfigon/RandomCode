__author__ = 'kamil'

import unittest
from Dodawanie import foo
from Dodawanie import czyPalidrom

class Dodawanie(unittest.TestCase):
    def test_28(self):
        self.assertEqual("121 2", foo(28))

    def test_5(self):
        self.assertEqual("5 0", foo(5))

    def test_68(self):
        self.assertEqual("1111 3", foo(68))

class PalidromTest(unittest.TestCase):
    def test_123(self):
        self.assertEqual(False, czyPalidrom(123))
    def test_122(self):
        self.assertEqual(False, czyPalidrom(122))
    def test_121(self):
        self.assertEqual(True, czyPalidrom(121))
    def test_5(self):
        self.assertEqual(True, czyPalidrom(5))

if __name__ == '__main__':
    unittest.main()
