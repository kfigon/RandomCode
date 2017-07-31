__author__ = 'kamil'

import unittest
from Procesor import Procesor
from Procesor import Reg

class MyTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.procesor = Procesor()
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R0))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R1))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R2))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R3))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R4))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R5))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R6))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R7))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R8))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R9))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R10))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R11))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R12))
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R13))
        self.assertEqual(0, self.procesor.getRejestr(Reg.Flow.PC))
        self.assertEqual(0, self.procesor.getRejestr(Reg.Flow.SP))

    def testGetRejestr0(self):
        self.assertEqual(0, self.procesor.getRejestr(Reg.GP.R0))

    def testGetRejestrTooBigOffset(self):
        self.assertRaises(IndexError, self.procesor.getRejestr, 16)

    def testGetRejestrNegativeOffset(self):
        self.assertRaises(IndexError, self.procesor.getRejestr, -1)

    def testGetAdres0(self):
        self.assertEqual(0, self.procesor.czytajAdres(0))

    def testGetAdresNegative(self):
        self.assertRaises(IndexError, self.procesor.czytajAdres, -1)

    def testTooBigAdres(self):
        self.assertRaises(IndexError, self.procesor.czytajAdres, 1024)

    def testWrite1_GetAdres0(self):
        self.procesor.zapiszPodAdres(0, 1)
        self.assertEqual(1, self.procesor.czytajAdres(0))

    def testSet(self):
        self.procesor.set(Reg.GP.R0, 1)
        self.assertEqual(1, self.procesor.getRejestr(Reg.GP.R0))

    def testSetNegativeOffset(self):
        self.assertRaises(IndexError, self.procesor.set, -1, 0)

    def testMov(self):
        self.procesor.set(Reg.GP.R0, 1)
        self.procesor.mov(Reg.GP.R1, Reg.GP.R0)

        self.assertEqual(1, self.procesor.getRejestr(Reg.GP.R1))
        self.assertEqual(1, self.procesor.getRejestr(Reg.GP.R0))

    def testLd(self):
        adres = 0xff
        wartosc = 0xde
        self.procesor.zapiszPodAdres(adres, wartosc)
        self.procesor.set(Reg.GP.R2, adres)
        self.procesor.ld(Reg.GP.R1, Reg.GP.R2)

        self.assertEqual(wartosc, self.procesor.getRejestr(Reg.GP.R1))

    def testSt(self):
        adres = 0xff
        wartosc = 0xde
        self.procesor.set(Reg.GP.R9, wartosc)
        self.procesor.set(Reg.GP.R1, adres)

        self.procesor.st(Reg.GP.R1, Reg.GP.R9)
        self.assertEqual(wartosc, self.procesor.czytajAdres(adres))

    def testAdd(self):
        a = 1
        b = 2
        self.procesor.set(Reg.GP.R0, a)
        self.procesor.set(Reg.GP.R1, b)

        self.procesor.add(Reg.GP.R1, Reg.GP.R0)

        self.assertEqual(a+b, self.procesor.getRejestr(Reg.GP.R1))

    def testSub(self):
        a = 5
        b = 1
        self.procesor.set(Reg.GP.R1, a)
        self.procesor.set(Reg.GP.R0, b)

        self.procesor.sub(Reg.GP.R1, Reg.GP.R0)

        self.assertEqual(a-b, self.procesor.getRejestr(Reg.GP.R1))

    def testMul(self):
        a = 3
        b = 4
        self.procesor.set(Reg.GP.R0, a)
        self.procesor.set(Reg.GP.R1, b)

        self.procesor.mul(Reg.GP.R1, Reg.GP.R0)

        self.assertEqual(a*b, self.procesor.getRejestr(Reg.GP.R1))

    def testMul_square(self):
        a = 3
        self.procesor.set(Reg.GP.R1, a)

        self.procesor.mul(Reg.GP.R1, Reg.GP.R1)

        self.assertEqual(a*a, self.procesor.getRejestr(Reg.GP.R1))

    def testDiv(self):
        a = 3
        b = 4
        self.procesor.set(Reg.GP.R0, a)
        self.procesor.set(Reg.GP.R1, b)

        self.procesor.div(Reg.GP.R1, Reg.GP.R0)

        self.assertEqual(a*b, self.procesor.getRejestr(Reg.GP.R1))


if __name__ == '__main__':
    unittest.main()
