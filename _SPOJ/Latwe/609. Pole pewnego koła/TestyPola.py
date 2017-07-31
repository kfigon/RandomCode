__author__ = 'kamil'

import unittest
from Pole import foo

class Pole(unittest.TestCase):
    def test_10_10(self):
        self.assertAlmostEqual(235.62, foo(10, 10), 2)

    def test_1000_1500(self):
        self.assertAlmostEqual(1374446.79, foo(1000, 1500),2)

if __name__ == '__main__':
    unittest.main()
