__author__ = 'kamil'

import unittest
from MgrRejestrPrzesuwny.foo import Rejestr

class MyTestCase(unittest.TestCase):
    def testDlugosci(self):
        reg = Rejestr(4,[3,2])
        self.assertEqual(2**4-1, reg.ileCiagowMoznaWyliczyc())

    def test1(self):
        reg = Rejestr(3, [3,2])
        self.assertEqual(2**3-1, reg.ileCiagowMoznaWyliczyc())

        #cyklicznie ten sam ciag
        for i in range(10):
            self.assertEqual(0, reg.get())
            self.assertEqual(0, reg.get())
            self.assertEqual(1, reg.get())
            self.assertEqual(0, reg.get())
            self.assertEqual(1, reg.get())
            self.assertEqual(1, reg.get())
            self.assertEqual(1, reg.get())

    def test2(self):
        reg = Rejestr(15, [15,13,9,8,7,5])
        self.assertEqual(2**15-1, reg.ileCiagowMoznaWyliczyc())

        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())

        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())

        self.assertEqual(1, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())

        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())

        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(0, reg.get())
        self.assertEqual(1, reg.get())

if __name__ == '__main__':
    unittest.main()
