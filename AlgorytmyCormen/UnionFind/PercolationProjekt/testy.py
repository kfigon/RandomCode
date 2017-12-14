__author__ = 'kamil'

import unittest
from AlgorytmyCormen.UnionFind.PercolationProjekt.KalkulatorWspolrzednych import *

class TestyKalkulatoraWpolrzednych(unittest.TestCase):
    def setUp(self):
        self.k = KalkulatorWspolrzednych(5,5, 10,10)

    def testPierwszyWiersz(self):
        self.assertEqual((0,0,9,9), self.k.get(0))
        self.assertEqual((10,0,19,9), self.k.get(1))
        self.assertEqual((20,0,29,9), self.k.get(2))
        self.assertEqual((30,0,39,9), self.k.get(3))
        self.assertEqual((40,0,49,9), self.k.get(4))

    def testDrugiWiersz(self):
        self.assertEqual((0,10,9,19), self.k.get(5))
        self.assertEqual((10,10,19,19), self.k.get(6))
        self.assertEqual((20,10,29,19), self.k.get(7))
        self.assertEqual((30,10,39,19), self.k.get(8))
        self.assertEqual((40,10,49,19), self.k.get(9))

    def testMappingTo2D(self):
        self.assertEqual((0,0), self.k.mapTo2D(0))
        self.assertEqual((0,1), self.k.mapTo2D(1))
        self.assertEqual((0,2), self.k.mapTo2D(2))
        self.assertEqual((0,3), self.k.mapTo2D(3))
        self.assertEqual((0,4), self.k.mapTo2D(4))

        self.assertEqual((1,0), self.k.mapTo2D(5))
        self.assertEqual((1,1), self.k.mapTo2D(6))
        self.assertEqual((1,2), self.k.mapTo2D(7))
        self.assertEqual((1,3), self.k.mapTo2D(8))
        self.assertEqual((1,4), self.k.mapTo2D(9))

        self.assertEqual((2,0), self.k.mapTo2D(10))
        self.assertEqual((2,1), self.k.mapTo2D(11))
        self.assertEqual((2,2), self.k.mapTo2D(12))

        self.assertEqual((3,0), self.k.mapTo2D(15))
        self.assertEqual((3,1), self.k.mapTo2D(16))
        self.assertEqual((3,4), self.k.mapTo2D(19))

        self.assertEqual((4,0), self.k.mapTo2D(20))
        self.assertEqual((4,4), self.k.mapTo2D(24))

if __name__ == '__main__':
    unittest.main()
