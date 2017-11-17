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
        p = Populacja(1000, self.celTab, 1)
        self.assertEqual(1000, p.getLiczebnoscPopulacji())

    def testLiczebnosciPoGenerowaniuPokolenia(self):
        p = Populacja(500, self.celTab, 1)
        p.generujNowePokolenie()
        self.assertEqual(500, p.getLiczebnoscPopulacji())


class TestPopulacjiEndToEnd(unittest.TestCase):
    def test(self):
        cel = "asd"
        celTab = str2Tab(cel)
        p = Populacja(500, celTab, 1)
        najlepszy = p.getNajlepszy()
        fitnessNajlepszego = najlepszy.liczFitness(celTab)
        nrPopulacji = 0
        while(fitnessNajlepszego < 100):
            p.generujNowePokolenie()
            nrPopulacji+=1
            najlepszy = p.getNajlepszy()
            fitnessNajlepszego = najlepszy.liczFitness(celTab)

        self.assertEqual(cel, str(najlepszy))
        print('nr populacji %d' % nrPopulacji)
        self.assertLess(nrPopulacji, 10)


class TestRuletki(unittest.TestCase):
    def setUp(self):
        # kolejno procenty:
        #    26  2  1  30  19  22, inkrementalnie:
        #     0  26 28 29  59  78  100
        tab=[70, 5, 3, 80, 50, 60]
        self.r = Ruletka(tab)

    def testNegatywny1(self):
        try:
            self.r.wybierzIndeksZwyciezcy(0)
        except Exception as e:
            pass
        else:
            self.fail("spodziewano sie wyjatku")

    def testNegatywny2(self):
        try:
            self.r.wybierzIndeksZwyciezcy(-1)
        except Exception as e:
            pass
        else:
            self.fail("spodziewano sie wyjatku")

    def testNegatywny3(self):
        try:
            self.r.wybierzIndeksZwyciezcy(101)
        except Exception as e:
            pass
        else:
            self.fail("spodziewano sie wyjatku")

    def testLosowaniaIdx0(self):
        self.assertEqual(0, self.r.wybierzIndeksZwyciezcy(1))
        self.assertEqual(0, self.r.wybierzIndeksZwyciezcy(3))
        self.assertEqual(0, self.r.wybierzIndeksZwyciezcy(5))
        self.assertEqual(0, self.r.wybierzIndeksZwyciezcy(8))
        self.assertEqual(0, self.r.wybierzIndeksZwyciezcy(10))
        self.assertEqual(0, self.r.wybierzIndeksZwyciezcy(15))
        self.assertEqual(0, self.r.wybierzIndeksZwyciezcy(20))
        self.assertEqual(0, self.r.wybierzIndeksZwyciezcy(26))

    def testLosowaniaIdx1(self):
        self.assertEqual(1, self.r.wybierzIndeksZwyciezcy(27))

    def testLosowaniaIdx2(self):
        self.assertEqual(2, self.r.wybierzIndeksZwyciezcy(28))
        self.assertEqual(2, self.r.wybierzIndeksZwyciezcy(29))

    def testLosowaniaIdx3(self):
        self.assertEqual(3, self.r.wybierzIndeksZwyciezcy(30))
        self.assertEqual(3, self.r.wybierzIndeksZwyciezcy(35))
        self.assertEqual(3, self.r.wybierzIndeksZwyciezcy(40))
        self.assertEqual(3, self.r.wybierzIndeksZwyciezcy(50))

    def testLosowaniaIdx4(self):
        self.assertEqual(4, self.r.wybierzIndeksZwyciezcy(59))
        self.assertEqual(4, self.r.wybierzIndeksZwyciezcy(60))

    def testLosowaniaIdx5(self):
        self.assertEqual(5, self.r.wybierzIndeksZwyciezcy(78))
        self.assertEqual(5, self.r.wybierzIndeksZwyciezcy(79))
        self.assertEqual(5, self.r.wybierzIndeksZwyciezcy(90))
        self.assertEqual(5, self.r.wybierzIndeksZwyciezcy(100))

if __name__ == '__main__':
    unittest.main()
