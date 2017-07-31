__author__ = 'kamil'


import unittest
from foo import foo



class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, foo(1))
    def test_2(self):
        self.assertEqual(1, foo(2))
    def test_8(self):
        self.assertEqual(3, foo(8))
    def test_3(self):
        self.assertEqual(7, foo(3))
    def test_567(self):
        self.assertEqual(61, foo(567))

if __name__ == '__main__':
    unittest.main()