__author__ = 'kamil'

import unittest
from foo import bar

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual('X', bar([['X', 1, 1]]))

    def test_3(self):
        self.assertEqual('A B C', bar([
            ['A', 0, 0],
            ['C', 5, 5],
            ['B', 1, -1]]))

if __name__ == '__main__':
    unittest.main()
