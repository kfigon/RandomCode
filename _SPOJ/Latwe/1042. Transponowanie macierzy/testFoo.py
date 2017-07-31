__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            [
            [1, 4, 3, 8],
            [2, 3, 4, 7],
            [5, 3, 9, 7]],

            foo([
                [1, 2, 5],
                [4, 3, 3],
                [3, 4, 9],
                [8, 7, 7]]))

    def test_2(self):
        self.assertEqual(
            [
            [1,3,5],
            [2,4,6]],

            foo([
                [1,2],
                [3,4],
                [5,6],
            ]))


if __name__ == '__main__':
    unittest.main()
