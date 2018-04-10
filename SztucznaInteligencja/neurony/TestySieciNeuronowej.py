__author__ = 'kamil'

import unittest
from SiecNeuronowa import *

class TestySieciNeuronowej(unittest.TestCase):
    def testBasic(self):
        s = SiecNeuronowa(2, 2, 1)
        wynik = s.zgaduj([1,0])[0]
        # wszystkie wagi sa na 0 i
        # mamy sigmoidy. Na wyjsciu jest wiec to:
        expectedWynik = 0.94056
        self.assertAlmostEqual(expectedWynik, wynik, 5)

        #xor = !AND + OR
        # + -> AND
    def test_XOR(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
