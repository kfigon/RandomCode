from MathStuff.Vector import Vector
import unittest
from math import sqrt
from math import pi

class TestyVectora(unittest.TestCase):
    def test1(self):
        v = Vector(1,2)
        self.assertEqual(1, v.getX())
        self.assertEqual(2, v.getY())
        self.assertEqual("(1,2)", str(v))

    def testEquality(self):
        v1 = Vector(1,2)
        v2 = Vector(1,2)
        self.assertEqual(v1,v2)
        self.assertTrue(v1==v2)

    def testNotEqual(self):
        v1 = Vector(2,2)
        v2 = Vector(1,2)
        self.assertNotEqual(v1,v2)
        self.assertFalse(v1==v2)

    def testDodawania(self):
        v1 = Vector(3,4)
        v2 = Vector(-1,5)
        expected = Vector(2, 9)
        self.assertEqual(expected, v1+v2)

    def testOdejmowania(self):
        v1 = Vector(3,4)
        v2 = Vector(-1,5)
        expected = Vector(4, -1)
        self.assertEqual(expected, v1-v2)

    def testDodajSkalar(self):
        v = Vector(3,4)
        self.assertEqual(Vector(5,6), v.dodajSkalar(2))

    def testOdejmijSkalar(self):
        v = Vector(3,4)
        self.assertEqual(Vector(1,2), v.odejmijSkalar(2))

    def testGetDlugosc(self):
        v=Vector(1,1)
        self.assertEqual(sqrt(2), v.getDlugosc())

    def testGetDlugosc2(self):
        v=Vector(1,2)
        self.assertEqual(sqrt(5), v.getDlugosc())

    def testMnozPrzezSkalar(self):
        v=Vector(1,2)
        self.assertEqual(Vector(2,4), v.mnoz(2))
        self.assertEqual(Vector(4,8), v.mnoz(4))

    def testDzielPrzezSkalar(self):
        v=Vector(4,6)
        self.assertEqual(Vector(2,3), v.dziel(2))

    def testGetKat1(self):
        self.assertEqual(0, Vector(1,0).getKat())
        self.assertEqual(0, Vector(6,0).getKat())

    def testGetKat2(self):
        self.assertEqual(pi, Vector(-1,0).getKat())
        self.assertEqual(pi, Vector(-6,0).getKat())

    def testGetKat3(self):
        self.assertEqual(pi/2, Vector(0,1).getKat())
        self.assertEqual(pi/2, Vector(0,6).getKat())

    def testGetKat4(self):
        self.assertEqual(-pi/2, Vector(0,-1).getKat())
        self.assertEqual(-pi/2, Vector(0,-6).getKat())

    def testGetPostacTrygonomentryczna(self):
        self.assertEqual((1,0), Vector(1,0).getPostacTrygonometryczna())

    def testStworzZModuluIKata1(self):
        v = Vector.stworzZModuluIKata(1,0)
        self.assertEqual(Vector(1,0), v)

    def testStworzZModuluIKata1(self):
        v = Vector.stworzZModuluIKata(1,0)
        self.assertEqual(Vector(1,0), v)

    def testObroc(self):
        v = Vector(1,0)
        obrocony = v.obroc(pi/2)
        expected = Vector(0,1)
        # almost equal na Vectorze nie zadziala, bo nie mam
        # metody abs()
        self.assertAlmostEqual(expected.getX(), obrocony.getX())
        self.assertAlmostEqual(expected.getY(), obrocony.getY())
        self.assertEqual(v.getDlugosc(), obrocony.getDlugosc())

    def testNormalizacji(self):
        wynik = Vector(3,4).normalizuj()
        self.assertEqual(Vector(3/5, 4/5), wynik)
        self.assertEqual(1, wynik.getDlugosc())

if __name__ == '__main__':
    unittest.main()