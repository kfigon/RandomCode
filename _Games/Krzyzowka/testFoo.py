__author__ = 'kamil'

import unittest
from foo import Krotka
from foo import Krzyzowka

class testKrotek(unittest.TestCase):

    def testWysunietych1(self):
        k = Krotka("", "abcd", 2)
        self.assertEqual(2, k.liczIleLiterIdzieWLewo())
        self.assertEqual(1, k.liczIleLiterIdzieWPrawo())

    def testWysunietych2(self):
        k = Krotka("", "abc", 1)
        self.assertEqual(1, k.liczIleLiterIdzieWLewo())
        self.assertEqual(1, k.liczIleLiterIdzieWPrawo())

    def testWysunietych3(self):
        k = Krotka("", "abc", 0)
        self.assertEqual(0, k.liczIleLiterIdzieWLewo())
        self.assertEqual(2, k.liczIleLiterIdzieWPrawo())

    def testWysunietych4(self):
        k = Krotka("", "ab", 1)
        self.assertEqual(1, k.liczIleLiterIdzieWLewo())
        self.assertEqual(0, k.liczIleLiterIdzieWPrawo())

    def testWysunietych5(self):
        k = Krotka("", "abcd", 1)
        self.assertEqual(1, k.liczIleLiterIdzieWLewo())
        self.assertEqual(2, k.liczIleLiterIdzieWPrawo())

class testyKrzyzowki(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.k = Krzyzowka()
        self.k.ladujKrotke(Krotka("","abcd", 2))
        self.k.ladujKrotke(Krotka("","abc", 1))
        self.k.ladujKrotke(Krotka("","abc", 0))
        self.k.ladujKrotke(Krotka("","ab", 1))
        self.k.ladujKrotke(Krotka("","abcd", 1))

    def testIleHasel(self):
        self.assertEqual(5, self.k.getIleHasel())

    def testWysunietaWLewo(self):
        kr = self.k.getNajbardziejWysunietaWLewoKrotka()
        self.assertEqual("abcd", kr.getHaslo())
        self.assertEqual(2, kr.getIndeks())
        self.assertEqual(self.k.getKrotka(0), kr)

    def testWysunietaWPrawo(self):
        kr = self.k.getNajbardziejWysunietaWPrawoKrotka()
        self.assertEqual("abc", kr.getHaslo())
        self.assertEqual(0, kr.getIndeks())
        self.assertEqual(self.k.getKrotka(2), kr)

    def testSzerokosc(self):
        self.assertEqual(5, self.k.getSzerokoscPlanszy())

    def testPozycjiGlownegoHasla(self):
        self.assertEqual(2, self.k.getPozycjaGlownegoHasla())

    def testOffsetu0(self):
        self.assertEqual(0, self.k.getOffsetDlaKrotki(0))
    def testOffsetu1(self):
        self.assertEqual(1, self.k.getOffsetDlaKrotki(1))
    def testOffsetu2(self):
        self.assertEqual(2, self.k.getOffsetDlaKrotki(2))
    def testOffsetu3(self):
        self.assertEqual(1, self.k.getOffsetDlaKrotki(3))
    def testOffsetu4(self):
        self.assertEqual(1, self.k.getOffsetDlaKrotki(4))

    def testGlownegoHasla(self):
        self.assertEqual("cbabb", self.k.getGlowneHaslo())

if __name__ == '__main__':
    unittest.main()
