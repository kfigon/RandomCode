__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
        [2,3,4,5,6,7,1], foo([1,2,3,4,5,6,7]))

    def test_2(self):
        self.assertEqual(
        [1,10,2], foo([2,1,10]))

if __name__ == '__main__':
    unittest.main()
