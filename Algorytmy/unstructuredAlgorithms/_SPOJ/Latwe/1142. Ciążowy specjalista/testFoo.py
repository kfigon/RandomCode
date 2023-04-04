__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(9, foo(21, 6, 5))
    def test_2(self):
        self.assertEqual(1, foo(11, 1, 13))
    def test_3(self):
        self.assertEqual(0, foo(223, 2, 113))


if __name__ == '__main__':
    unittest.main()
