__author__ = 'kamil'

import unittest
from Music.Nuta import *
from Music.Akord import *

class TestyNut(unittest.TestCase):
    def __internalTest(self, testName, noteVal, noteStr):
        n = Nuta(noteVal)
        self.assertEqual(noteVal, n.get(), "%s failed: expected %d, exact %d" % (testName, noteVal, n.get()))
        self.assertEqual(noteStr, str(n), "%s failed: expected %s, exact %s" % (testName, noteStr, str(n)))

    def testNut(self):
        self.__internalTest("test C", Nuta.C, "C")
        self.__internalTest("test Cis", Nuta.Cis, "Cis")
        self.__internalTest("test D", Nuta.D, "D")
        self.__internalTest("test Dis", Nuta.Dis, "Dis")
        self.__internalTest("test E", Nuta.E, "E")
        self.__internalTest("test F", Nuta.F, "F")
        self.__internalTest("test Fis", Nuta.Fis, "Fis")
        self.__internalTest("test G", Nuta.G, "G")
        self.__internalTest("test Gis", Nuta.Gis, "Gis")
        self.__internalTest("test A", Nuta.A, "A")
        self.__internalTest("test Ais", Nuta.Ais, "Ais")
        self.__internalTest("test B", Nuta.B, "B")

    def testInvalidValue(self):
        try:
            n = Nuta(-1)
        except Exception as e:
            pass
        else:
            self.fail("missing exception")

    def testInvalidValue2(self):
        try:
            n = Nuta(12)
        except Exception as e:
            pass
        else:
            self.fail("missing exception")

    def testEquality(self):
        n = Nuta(Nuta.Dis)
        self.assertEqual(Nuta(Nuta.Dis), n)

    def testGetInterval1(self):
        c = Nuta(Nuta.C)
        d = Nuta(Nuta.D)
        i = c.getInterval(d)
        self.assertEqual(Interwal.SekundaWielka, i.get())

    def testGetInterval2(self):
        g = Nuta(Nuta.G)
        c = Nuta(Nuta.C)
        i = g.getInterval(c)
        self.assertEqual(Interwal.Kwarta, i.get())
        self.assertEqual(Interwal.Kwinta, c.getInterval(g).get())

    def testGetInterval3(self):
        f = Nuta(Nuta.F)
        g = Nuta(Nuta.G)
        i = f.getInterval(g)
        self.assertEqual(Interwal.SekundaWielka, i.get())
        self.assertEqual(Interwal.SeptymaMala, g.getInterval(f).get())

class TestInterwalow(unittest.TestCase):
    def __internalTest(self, testName, intervalVal, intervalName):
        i = Interwal(intervalVal)
        self.assertEqual(intervalVal, i.get(), "%s failed: expected %d, exact %d" % (testName, intervalVal, i.get()))
        self.assertEqual(intervalName, str(i), "%s failed: expected %s, exact %s" % (testName, intervalName, str(i)))

    def testInterwalow(self):
        self.__internalTest("test pryma", Interwal.Pryma, "Pryma")
        self.__internalTest("test sekunda mala", Interwal.SekundaMala, "Sekunda Mala")
        self.__internalTest("test sekunda wielka", Interwal.SekundaWielka, "Sekunda Wielka")
        self.__internalTest("test tercja mala", Interwal.TercjaMala, "Tercja Mala")
        self.__internalTest("test tercja wielka", Interwal.TercjaWielka, "Tercja Wielka")
        self.__internalTest("test kwarta", Interwal.Kwarta, "Kwarta")
        self.__internalTest("test tryton", Interwal.Tryton, "Tryton")
        self.__internalTest("test kwinta", Interwal.Kwinta, "Kwinta")
        self.__internalTest("test seksta mala", Interwal.SekstaMala, "Seksta Mala")
        self.__internalTest("test seksta wielka", Interwal.SekstaWielka, "Seksta Wielka")
        self.__internalTest("test septyma mala", Interwal.SeptymaMala, "Septyma Mala")
        self.__internalTest("test septyma wielka", Interwal.SeptymaWielka, "Septyma Wielka")
        self.__internalTest("test oktawa", Interwal.Oktawa, "Pryma")

    def testInvalidValue(self):
        try:
            n = Nuta(-1)
        except Exception as e:
            pass
        else:
            self.fail("missing exception")

    def testTooBigVal(self):
        self.__internalTest("test nona", Interwal.NonaMala, "Sekunda Mala")
        self.__internalTest("test duodecyma", 7, "Kwinta")

class TestNutyZInterwalow(unittest.TestCase):
    def __internalTest(self, startNote, halfstepsNumber, expectedStopNote):
        n = Nuta(startNote)
        interval = Interwal(halfstepsNumber)
        newNote = n.getNoteFromInterval(interval)
        self.assertEqual(expectedStopNote, newNote.get(),
                         "%s od %s, expected %s, actual %s" % (str(interval),str(Nuta(startNote)), str(Nuta(expectedStopNote)),str(newNote)))

    def testC(self):
        self.__internalTest(Nuta.C, Interwal.SekundaMala, Nuta.Cis)
        self.__internalTest(Nuta.C, Interwal.SekundaWielka, Nuta.D)
        self.__internalTest(Nuta.C, Interwal.TercjaMala, Nuta.Dis)
        self.__internalTest(Nuta.C, Interwal.TercjaWielka, Nuta.E)
        self.__internalTest(Nuta.C, Interwal.Kwarta, Nuta.F)
        self.__internalTest(Nuta.C, Interwal.Tryton, Nuta.Fis)
        self.__internalTest(Nuta.C, Interwal.Kwinta, Nuta.G)
        self.__internalTest(Nuta.C, Interwal.SekstaMala, Nuta.Gis)
        self.__internalTest(Nuta.C, Interwal.SekstaWielka, Nuta.A)
        self.__internalTest(Nuta.C, Interwal.SeptymaMala, Nuta.Ais)
        self.__internalTest(Nuta.C, Interwal.SeptymaWielka, Nuta.B)

        self.__internalTest(Nuta.C, Interwal.Oktawa, Nuta.C)
        self.__internalTest(Nuta.C, Interwal.NonaMala, Nuta.Cis)
        self.__internalTest(Nuta.C, Interwal.NonaWielka, Nuta.D)
        self.__internalTest(Nuta.C, Interwal.DecymaMala, Nuta.Dis)
        self.__internalTest(Nuta.C, Interwal.DecymaWielka, Nuta.E)
        self.__internalTest(Nuta.C, Interwal.Undecyma, Nuta.F)
        self.__internalTest(Nuta.C, Interwal.UndecymaZwiekszona, Nuta.Fis)
        # skip tryton
        self.__internalTest(Nuta.C, Interwal.TerdecymaMala, Nuta.Gis)
        self.__internalTest(Nuta.C, Interwal.TerdecymaWielka, Nuta.A)
        self.__internalTest(Nuta.C, 24, Nuta.C)
        self.__internalTest(Nuta.C, 25, Nuta.Cis)

    def testA(self):
        self.__internalTest(Nuta.A, Interwal.SekundaMala, Nuta.Ais)
        self.__internalTest(Nuta.A, Interwal.SekundaWielka, Nuta.B)
        self.__internalTest(Nuta.A, Interwal.TercjaMala, Nuta.C)
        self.__internalTest(Nuta.A, Interwal.TercjaWielka, Nuta.Cis)
        self.__internalTest(Nuta.A, Interwal.Kwarta, Nuta.D)
        self.__internalTest(Nuta.A, Interwal.Tryton, Nuta.Dis)
        self.__internalTest(Nuta.A, Interwal.Kwinta, Nuta.E)
        self.__internalTest(Nuta.A, Interwal.SekstaMala, Nuta.F)
        self.__internalTest(Nuta.A, Interwal.SekstaWielka, Nuta.Fis)
        self.__internalTest(Nuta.A, Interwal.SeptymaMala, Nuta.G)
        self.__internalTest(Nuta.A, Interwal.SeptymaWielka, Nuta.Gis)

        self.__internalTest(Nuta.A, Interwal.Oktawa, Nuta.A)
        self.__internalTest(Nuta.A, Interwal.NonaMala, Nuta.Ais)
        self.__internalTest(Nuta.A, Interwal.NonaWielka, Nuta.B)
        self.__internalTest(Nuta.A, Interwal.DecymaMala, Nuta.C)
        self.__internalTest(Nuta.A, Interwal.DecymaWielka, Nuta.Cis)
        self.__internalTest(Nuta.A, Interwal.Undecyma, Nuta.D)
        self.__internalTest(Nuta.A, Interwal.UndecymaZwiekszona, Nuta.Dis)
        #skip tryton
        self.__internalTest(Nuta.A, Interwal.TerdecymaMala, Nuta.F)
        self.__internalTest(Nuta.A, Interwal.TerdecymaWielka, Nuta.Fis)
        self.__internalTest(Nuta.A, 24, Nuta.A)
        self.__internalTest(Nuta.A, 25, Nuta.Ais)

    def testB(self):
        self.__internalTest(Nuta.B, Interwal.SekundaMala, Nuta.C)
        self.__internalTest(Nuta.B, Interwal.SekundaWielka, Nuta.Cis)
        self.__internalTest(Nuta.B, Interwal.TercjaMala, Nuta.D)
        self.__internalTest(Nuta.B, Interwal.TercjaWielka, Nuta.Dis)
        self.__internalTest(Nuta.B, Interwal.Kwarta, Nuta.E)
        self.__internalTest(Nuta.B, Interwal.Tryton, Nuta.F)
        self.__internalTest(Nuta.B, Interwal.Kwinta, Nuta.Fis)
        self.__internalTest(Nuta.B, Interwal.SekstaMala, Nuta.G)
        self.__internalTest(Nuta.B, Interwal.SekstaWielka, Nuta.Gis)
        self.__internalTest(Nuta.B, Interwal.SeptymaMala, Nuta.A)
        self.__internalTest(Nuta.B, Interwal.SeptymaWielka, Nuta.Ais)

        self.__internalTest(Nuta.B, Interwal.Oktawa, Nuta.B)
        self.__internalTest(Nuta.B, Interwal.NonaMala, Nuta.C)
        self.__internalTest(Nuta.B, Interwal.NonaWielka, Nuta.Cis)
        self.__internalTest(Nuta.B, Interwal.DecymaMala, Nuta.D)
        self.__internalTest(Nuta.B, Interwal.DecymaWielka, Nuta.Dis)
        self.__internalTest(Nuta.B, Interwal.Undecyma, Nuta.E)
        self.__internalTest(Nuta.B, Interwal.UndecymaZwiekszona, Nuta.F)
        #skip tryton
        self.__internalTest(Nuta.B, Interwal.TerdecymaMala, Nuta.G)
        self.__internalTest(Nuta.B, Interwal.TerdecymaWielka, Nuta.Gis)
        self.__internalTest(Nuta.B, 24, Nuta.B)
        self.__internalTest(Nuta.B, 25, Nuta.C)

class TestSkal(unittest.TestCase):
    def __internal(self, skala, expectedNotes, expectedStr):
        gama = skala.get()
        self.assertEqual(len(expectedNotes), len(gama))
        for i in range(len(gama)):
            self.assertEqual(expectedNotes[i].get(), gama[i].get())

        self.assertEqual(expectedStr, str(skala))

    def testCdur(self):
        expected = [Nuta(Nuta.C), Nuta(Nuta.D),Nuta(Nuta.E),
                    Nuta(Nuta.F),Nuta(Nuta.G),Nuta(Nuta.A),
                    Nuta(Nuta.B)]
        s = GamaDurowa(Nuta(Nuta.C))
        self.__internal(s, expected, "C, D, E, F, G, A, B")

    def testGdur(self):
        expected = [Nuta(Nuta.G), Nuta(Nuta.A),Nuta(Nuta.B),
                    Nuta(Nuta.C),Nuta(Nuta.D),Nuta(Nuta.E),
                    Nuta(Nuta.Fis)]
        s = GamaDurowa(Nuta(Nuta.G))
        self.__internal(s, expected, "G, A, B, C, D, E, Fis")

    def testAmol(self):
        expected = [Nuta(Nuta.A), Nuta(Nuta.B),Nuta(Nuta.C),
                    Nuta(Nuta.D),Nuta(Nuta.E),Nuta(Nuta.F),
                    Nuta(Nuta.G)]
        s = GamaMolowa(Nuta(Nuta.A))
        self.__internal(s, expected, "A, B, C, D, E, F, G")

class TestAkordow(unittest.TestCase):
    def testCdur(self):
        c = Akord([Nuta(Nuta.C), Nuta(Nuta.E), Nuta(Nuta.G)])
        self.assertEqual("Cdur", str(c))
        self.assertEqual(TrybAkordu.Dur, c.getTryb())
        self.assertEqual(RodzajAkordu.BrakSeptymy, c.getRodzaj())

    def testMoreStuff(self):
        self.fail("to implement")

class TestAkordBuildera(unittest.TestCase):
    def test(self):
        self.fail('to implement')

if __name__ == '__main__':
    unittest.main()
