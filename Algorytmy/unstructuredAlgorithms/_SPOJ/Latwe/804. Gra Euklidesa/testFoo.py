__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test_11(self):
        self.assertEqual(2, foo(1,1))
    def test_24(self):
        self.assertEqual(4, foo(2,4))
    def test_96(self):
        self.assertEqual(6, foo(9,6))

if __name__ == '__main__':
    unittest.main()