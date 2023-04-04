__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, foo(0.3, 0.3, 0.4))

    def test_2(self):
        self.assertEqual(2, foo(-0.5, -0.5, 0))

    def test_3(self):
        self.assertEqual(1, foo(0.5, 1, 0.5))


if __name__ == '__main__':
    unittest.main()
