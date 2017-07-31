__author__ = 'kamil'

import unittest
from foo import foo
from foo import przesunGore
from foo import przesunDol

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual([
            [2,3,6],
            [1,5,9],
            [4,7,8]],
                foo([
                [1,2,3],
                [4,5,6],
                [7,8,9]]))

    def test_2(self):
        self.assertEqual([
            [2,3,4,8],
            [1,6,7,12],
            [5,9,10,11]],
                foo([
                [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]]))

    def test_3(self):
        self.assertEqual([
            [2,3,4,5,0],
            [1,7,8,9,5],
            [6,1,2,3,4]],
                         foo([
                            [1,2,3,4,5],
                            [6,7,8,9,0],
                            [1,2,3,4,5]]))

    def test_gora(self):
        self.assertEqual([
            [2,3,1],
            [4,5,6],
            [7,8,9]
        ], przesunGore([
                [1,2,3],
                [4,5,6],
                [7,8,9]]))

    def test_dol(self):
        self.assertEqual([
            [1,2,3],
            [4,5,6],
            [9,7,8]
        ], przesunDol([
                [1,2,3],
                [4,5,6],
                [7,8,9]]))

if __name__ == '__main__':
    unittest.main()
