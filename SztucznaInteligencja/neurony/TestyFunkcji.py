__author__ = 'kamil'

import unittest
from Funkcje import *

class TestyFunkcji(unittest.TestCase):
    def test_Generyczna(self):
        f = Funkcja()
        self.assertEqual(0, f.get(4))

    def test_Liniowa(self):
        f = FunkcjaLiniowa(3,5)
        self.assertEqual(17, f.get(4))

    def test_Sigmoida(self):
        f = Sigmoida()
        self.assertEqual(0, f.get(-10))
        self.assertEqual(1, f.get(10))
        self.assertAlmostEqual(0.5, f.get(0))
        self.assertAlmostEqual(0.6225, f.get(0.5),4)

    def test_Signum(self):
        f = Signum()
        self.assertEqual(-1, f.get(-5))
        self.assertEqual(-1, f.get(-4))
        self.assertEqual(-1, f.get(-3))
        self.assertEqual(-1, f.get(-2))
        self.assertEqual(-1, f.get(-1))
        self.assertEqual(1, f.get(0))
        self.assertEqual(1, f.get(1))
        self.assertEqual(1, f.get(2))
        self.assertEqual(1, f.get(3))

if __name__ == '__main__':
    unittest.main()
