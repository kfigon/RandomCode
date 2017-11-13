__author__ = 'kamil'

import unittest
from SztucznaInteligencja.utils import *

class TestyPerceptrona(unittest.TestCase):
    def setUp(self):
        self.p = Perceptron(2)

    def test_GetFunkcja(self):
        # funkcja liniowa z parametrow 1,1,1
        #                              w0,w1,stala
        f = self.p.getFunkcjaLiniowa()
        self.assertIsInstance(f, FunkcjaLiniowa)
        self.assertEqual(-1, f.get(0))
        # -1*x - 1
        self.assertEqual(-6, f.get(5))
    def test_toStr(self):
        self.assertEqual("w0: 1, w1: 1, bias: 1", str(self.p))

    def test_zgaduj(self):
        self.assertEqual(1, self.p.zgaduj([2,4]),4)
        self.assertEqual(-1, self.p.zgaduj([-2,-4]),3)
        self.assertEqual(-1, self.p.zgaduj([2,-13]),4)
        self.assertEqual(1, self.p.zgaduj([84,4]),4)

class TestyPredykcji(unittest.TestCase):
    def setUp(self):
        self.p = Perceptron(2)

    def jedziesz(self, funkcjaLiniowa):
        dane = generujDane(5000, funkcjaLiniowa)
        trening(self.p, dane)
        procentBledow = sprawdzIleBledow(self.p, dane)
        self.assertLess(procentBledow, 15)

    def test_bezTreningu(self):
        dane = generujDane(1000, FunkcjaLiniowa(1,1))
        procentBledow = sprawdzIleBledow(self.p, dane)
        self.assertGreater(procentBledow, 20)

    def test_basicLinia(self):
        self.jedziesz(FunkcjaLiniowa(1,0))
    def test_basicLinia2(self):
        self.jedziesz(FunkcjaLiniowa(8,100))
    def test_basicLinia2(self):
        self.jedziesz(FunkcjaLiniowa(8,100))
    def test_basicLinia3(self):
        self.jedziesz(FunkcjaLiniowa(-10,100))
    def test_basicLinia4(self):
        self.jedziesz(FunkcjaLiniowa(8,-100))
    def test_basicLinia5(self):
        self.jedziesz(FunkcjaLiniowa(0,100))
    def test_basicLinia6(self):
        self.jedziesz(FunkcjaLiniowa(0,-80))

    #0,0->0
    #0,1->0
    #1,0->0
    #1,1->1
    def test_AND(self):
        dane=[{'x':0,'y':0,'klasa':-1},
              {'x':0,'y':1,'klasa':-1},
              {'x':1,'y':0,'klasa':-1},
              {'x':1,'y':1,'klasa':1}]*50
        for d in dane:
            self.p.trenuj(toVector(d), d['klasa'])

        self.assertEquals(-1, self.p.zgaduj([0,0]))
        self.assertEquals(-1, self.p.zgaduj([0,1]))
        self.assertEquals(-1, self.p.zgaduj([1,0]))
        self.assertEquals(1, self.p.zgaduj([1,1]))
    #0,0->0
    #0,1->1
    #1,0->1
    #1,1->1
    def test_OR(self):
        dane=[{'x':0,'y':0,'klasa':-1},
              {'x':0,'y':1,'klasa':1},
              {'x':1,'y':0,'klasa':1},
              {'x':1,'y':1,'klasa':1}]*50
        for d in dane:
            self.p.trenuj(toVector(d), d['klasa'])

        self.assertEquals(-1, self.p.zgaduj([0,0]))
        self.assertEquals(1, self.p.zgaduj([0,1]))
        self.assertEquals(1, self.p.zgaduj([1,0]))
        self.assertEquals(1, self.p.zgaduj([1,1]))

    #xor = !AND + OR
        # + -> AND
if __name__ == '__main__':
    unittest.main()
