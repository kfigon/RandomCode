__author__ = 'kamil'

import unittest
from Obzartuchy import foo

class Testy(unittest.TestCase):
    def test_1(self):
        self.assertEqual(8, foo([3600, 1800], 10))

    def test_2(self):
        self.assertEqual(2, foo([123, 32999, 10101], 356))

if __name__ == '__main__':
    unittest.main()
