__author__ = 'kamil'

import unittest
from AlgorytmyCormen.UnionFind.PercolationProjekt.KalkulatorWspolrzednych import *
from AlgorytmyCormen.UnionFind.PercolationProjekt.Plansza import Plansza


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

class TestyPlanszy(unittest.TestCase):
    def setUp(self):
        self.p = Plansza(0)
        tab=[False,False,True,False,True,
             True,False,True,False,False,
             True,False,True,True,False,
             False,False,False,True,True,
             True,True,False,True,True]
        self.p.wstrzyknijTablice(tab)

    def testSasiadujace0(self):
        self.assertEqual([1,5], self.p.getSasiadujace(0))

    def testSasiadujace1(self):
        self.assertEqual([0,2,6], self.p.getSasiadujace(1))

    def testSasiadujace4(self):
        self.assertEqual([3,9], self.p.getSasiadujace(4))

    def testSasiadujace5(self):
        self.assertEqual([0,6,10], self.p.getSasiadujace(5))

    def testSasiadujace9(self):
        self.assertEqual([4,8,14], self.p.getSasiadujace(9))

    def testSasiadujace20(self):
        self.assertEqual([15,21], self.p.getSasiadujace(20))

    def testSasiadujace21(self):
        self.assertEqual([16,20,22], self.p.getSasiadujace(21))

    def testSasiadujace24(self):
        self.assertEqual([19,23], self.p.getSasiadujace(24))

    def testSasiadujace12(self):
        self.assertEqual([7,11,13,17], self.p.getSasiadujace(12))

    def testPercolation(self):
        self.assertTrue(self.p.czyJestPrzejscie())

if __name__ == '__main__':
    unittest.main()
