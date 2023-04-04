__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual([2, 5, 1, 3],
                         foo([1, 2, 3, 5]))

    def test_2(self):
        self.assertEqual([8, 9, 7],
                         foo([9, 8, 7]))


if __name__ == '__main__':
    unittest.main()
