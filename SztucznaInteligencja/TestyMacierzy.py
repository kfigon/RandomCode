__author__ = 'kamil'

import unittest
from SztucznaInteligencja.Macierz import *

class TestyMacierzy(unittest.TestCase):
    def testInicjalizacjiMacierza(self):
        m = Macierz([1,2,3],[4,5,6],[1,5,9],[0,0,0])
        self.assertEquals(4, m.getIloscWierszy())
        self.assertEquals(3, m.getIloscKolumn())

    def testInicjalizacjiMacierza2(self):
        m = Macierz([1,2,3],
                    [4,5,6])
        self.assertEquals(2, m.getIloscWierszy())
        self.assertEquals(3, m.getIloscKolumn())
    def testInitMacierzy3(self):
        # tutaj owija taba tuplem :(
        tab = [[1,2,3],[4,5,6]]
        m = Macierz(tab)
        self.assertEquals(2, m.getIloscWierszy())
        self.assertEquals(3, m.getIloscKolumn())
    def testInitMacierzy4(self):
        tab = [[1,2,3]]
        m = Macierz(tab)
        self.assertEquals(1, m.getIloscWierszy())
        self.assertEquals(3, m.getIloscKolumn())
    def testInitMacierzy5(self):
        m = Macierz([[1,2,3]])
        self.assertEquals(1, m.getIloscWierszy())
        self.assertEquals(3, m.getIloscKolumn())

    def testGetEl(self):
        m = Macierz([1,2,3],
                    [4,5,6])

        self.assertEquals(1, m.get(0,0))
        self.assertEquals(2, m.get(0,1))
        self.assertEquals(3, m.get(0,2))

        self.assertEquals(4, m.get(1,0))
        self.assertEquals(5, m.get(1,1))
        self.assertEquals(6, m.get(1,2))

    def testDodawania(self):
        m1 = Macierz([1,2,3],
                    [4,5,6])
        m2 = Macierz([0,5,3],
                    [6,7,3])
        m1.dodaj(m2)
        self.assertEquals(1, m1.get(0,0))
        self.assertEquals(7, m1.get(0,1))
        self.assertEquals(6, m1.get(0,2))

        self.assertEquals(10, m1.get(1,0))
        self.assertEquals(12, m1.get(1,1))
        self.assertEquals(9, m1.get(1,2))

    def testDodawaniaNiewlasciwychRozmiarow(self):
        m1 = Macierz([1,2,3],
                    [4,5,6])
        m2 = Macierz([0,5,3,4],
                    [6,7,3,5])

        self.assertEquals(2, m1.getIloscWierszy())
        self.assertEquals(3, m1.getIloscKolumn())

        self.assertEquals(2, m2.getIloscWierszy())
        self.assertEquals(4, m2.getIloscKolumn())
        try:
            m1.dodaj(m2)
        except Exception as e:
            pass
        else:
            self.fail("spodziewano sie wyjatku")

    def testOdejmowania(self):
        m1 = Macierz([1,2,3],
                    [4,5,6])
        m2 = Macierz([0,5,3],
                    [6,7,3])
        m1.odejmij(m2)
        self.assertEquals(1, m1.get(0,0))
        self.assertEquals(-3, m1.get(0,1))
        self.assertEquals(0, m1.get(0,2))

        self.assertEquals(-2, m1.get(1,0))
        self.assertEquals(-2, m1.get(1,1))
        self.assertEquals(3, m1.get(1,2))

    def testMnozeniaPrzezStala(self):
        m = Macierz([1,2,3],
                    [5,4,3])
        m.mnoz(5)
        self.assertEquals(5, m.get(0,0))
        self.assertEquals(10, m.get(0,1))
        self.assertEquals(15, m.get(0,2))

        self.assertEquals(25, m.get(1,0))
        self.assertEquals(20, m.get(1,1))
        self.assertEquals(15, m.get(1,2))

    def testMnozeniaPoElemencie(self):
        m1 = Macierz([1,2,3],
                    [4,5,6])
        m2 = Macierz([0,5,3],
                    [6,7,3])

        m1.mnozeMacierzeElementPoElemencie(m2)
        self.assertEquals(0, m1.get(0,0))
        self.assertEquals(10, m1.get(0,1))
        self.assertEquals(9, m1.get(0,2))

        self.assertEquals(24, m1.get(1,0))
        self.assertEquals(35, m1.get(1,1))
        self.assertEquals(18, m1.get(1,2))
    def testCzyMoznaMnozycMacierze(self):
        self.assertTrue(Macierz.czyMoznaMnozycMacierze(2,3,3,2))
        self.assertTrue(Macierz.czyMoznaMnozycMacierze(4,2,2,3))
        self.assertTrue(Macierz.czyMoznaMnozycMacierze(3,3,3,2))

        self.assertFalse(Macierz.czyMoznaMnozycMacierze(3,2,3,2))
    def testRozmiaruPoMnozeniu(self):
        self.assertEqual((2,2), Macierz.rozmiaryPoWymnozeniu(2,3,3,2))
        self.assertEqual((4,3), Macierz.rozmiaryPoWymnozeniu(4,2,2,3))
        self.assertEqual((3,2), Macierz.rozmiaryPoWymnozeniu(3,3,3,2))

    def testTranspozycji(self):
        self.fail('to implement')

    def testMnozenia(self):
        m1 = Macierz([1,0,2],
                     [-1,3,1])

        m2 = Macierz([3,1],
                     [2,1],
                     [1,0])
        # tuple issue
        m3 = m1.mnozMacierze(m2)

        self.assertEqual(2, m3.getIloscWierszy())
        self.assertEqual(2, m3.getIloscKolumn())

        self.assertEqual(5, m3.get(0,0))
        self.assertEqual(1, m3.get(0,1))
        self.assertEqual(4, m3.get(1,0))
        self.assertEqual(2, m3.get(1,1))

if __name__ == '__main__':
    unittest.main()
