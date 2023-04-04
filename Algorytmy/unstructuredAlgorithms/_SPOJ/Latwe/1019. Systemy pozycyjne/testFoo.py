__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual("4EF A49", foo(1263))

    def test_2(self):
        self.assertEqual("A A", foo(10))

if __name__ == '__main__':
    unittest.main()
