__author__ = 'kamil'

import unittest
from Parkometr import Parkometrx

class testyParkometru(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.p = Parkometrx(3) # 3 zl za godzine
        self.assertEqual(0, self.p.getIleMinut())

        godziny,minuty = self.p.getIleGodzinIMinut()
        self.assertEqual(0, godziny)
        self.assertEqual(0, minuty)

    def testNic(self):
        self.assertEqual(0, self.p.liczIle())

    def test15min(self):
        p = self.p
        p.zwiekszMinuty()
        self.assertEqual(0.75, p.liczIle())

    def testZwieksz(self):
        p = self.p
        p.zwiekszMinuty()
        self.assertEqual(15, p.getIleMinut())

        p.zwiekszMinuty()
        self.assertEqual(30, p.getIleMinut())

    def testZmniejsz(self):
        p = self.p
        p.zmniejszMinuty()
        self.assertEqual(0, p.getIleMinut())

        p.zmniejszMinuty()
        self.assertEqual(0, p.getIleMinut())

    def testZwiekszZmniejsz(self):
        p = self.p
        p.zwiekszMinuty()
        self.assertEqual(15, p.getIleMinut())

        p.zwiekszMinuty()
        self.assertEqual(30, p.getIleMinut())

        p.zmniejszMinuty()
        self.assertEqual(15, p.getIleMinut())
        p.zmniejszMinuty()
        self.assertEqual(0, p.getIleMinut())

    def testZwiekszGodzine(self):
        p = self.p
        p.zwiekszGodzine()
        self.assertEqual(60, p.getIleMinut())
        self.assertEqual(3, p.liczIle())

    def testZmniejszGodzine(self):
        p = self.p
        p.zwiekszGodzine()
        p.zwiekszMinuty()
        self.assertEqual(75, p.getIleMinut())

        p.zmniejszGodzine()
        self.assertEqual(15, p.getIleMinut())
        p.zmniejszGodzine()
        self.assertEqual(0, p.getIleMinut())

    def testGodzinIMinut1(self):
        self.p.zwiekszGodzine()
        g,m = self.p.getIleGodzinIMinut()
        self.assertEqual(1, g)
        self.assertEqual(0, m)

    def testGodzinIMinut2(self):
        self.p.zwiekszGodzine()
        self.p.zwiekszMinuty()
        g,m = self.p.getIleGodzinIMinut()
        self.assertEqual(1, g)
        self.assertEqual(15, m)

    def testGodzinIMinut3(self):
        self.p.zwiekszGodzine()
        self.p.zwiekszMinuty()
        self.p.zwiekszGodzine()
        g,m = self.p.getIleGodzinIMinut()
        self.assertEqual(2, g)
        self.assertEqual(15, m)

    def testGodzinIMinut4(self):
        self.p.zwiekszGodzine()
        self.p.zwiekszMinuty()
        self.p.zwiekszMinuty()
        g,m = self.p.getIleGodzinIMinut()
        self.assertEqual(1, g)
        self.assertEqual(30, m)


if __name__ == '__main__':
    unittest.main()
