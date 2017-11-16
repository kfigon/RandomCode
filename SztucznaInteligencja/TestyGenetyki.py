__author__ = 'kamil'

import unittest
from SztucznaInteligencja.AlgorytmyGenetyczne import *

class TestyGentyki(unittest.TestCase):
    def testInit(self):
        c  = Chromosom()
        self.assertEqual("", str(c))

    def testInit2(self):
        c  = Chromosom(str2Tab("napis napis"))
        self.assertEqual("napis napis", str(c))
        self.assertEqual(11, c.getDlugosc())

    def testStringToTab(self):
        self.assertEqual(['n','a','p','i','s'], str2Tab("napis"))

    def testRandomize(self):
        c = Chromosom()
        c.randomize(30)
        self.assertEqual(30, c.getDlugosc())
        self.assertNotEqual("malo prawdopodobny napis", str(c))

    def testFitnessu(self):
        ideal=str2Tab("napisikk")
        c = Chromosom(ideal)
        self.assertEqual(100, c.liczFitness(ideal))
        nieIdeal = str2Tab("ngpasgky")
        self.assertEqual(50, c.liczFitness(nieIdeal))

    def testKrzyzowania(self):
        c1 = Chromosom(str2Tab("unijorm"))
        c2 = Chromosom(str2Tab("popcorn"))

        c3 = c1.krzyzuj(c2, 3)
        self.assertEqual("unicorn", str(c3))
        self.assertEqual("unijorm", str(c1))
        self.assertEqual("popcorn", str(c2))

    def testMutowania100(self):
        c = Chromosom(str2Tab("napis"))
        c.mutuj(100)
        self.assertEqual(5, c.getDlugosc())
        self.assertNotEqual("napis", str(c))

    def testMutowania0(self):
        c = Chromosom(str2Tab("napis"))
        c.mutuj(0)
        self.assertEqual(5, c.getDlugosc())
        self.assertEqual("napis", str(c))

class TestyPopulacji(unittest.TestCase):
    def setUp(self):
        self.cel = "byc albo nie byc"
        self.celTab = str2Tab(self.cel)

    def testLiczebnosci(self):
        p = Populacja(1000, len(self.celTab),self.celTab, 1)
        self.assertEqual(1000, p.getLiczebnoscPopulacji())

    def testLiczebnosciPoGenerowaniuPokolenia(self):
        p = Populacja(1000, len(self.celTab), 1)
        p.generujNowePokolenie()
        self.assertEqual(1000, p.getLiczebnoscPopulacji())

    def testRuletki(self):
        # p = Populacja(5, len(self.celTab),self.celTab, 1)
        # p.wybierzXNajlepszych(2)
        self.fail('to do')

if __name__ == '__main__':
    unittest.main()
