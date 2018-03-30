import unittest
from ewaluatorWyrazen import *

class TestyPermutacji(unittest.TestCase):
    def testLogic1(self):
        g = GeneratorLogiki()
        expected=[[False],[True]]
        self.assertEqual(expected, g.generuj(1))

    def testLogic2(self):
        g = GeneratorLogiki()
        expected=[[False,False],
                  [False,True],
                  [True,False],
                  [True, True]]
        self.assertEqual(expected, g.generuj(2))

    def testLogic3(self):
        g = GeneratorLogiki()
        expected=[[False,False,False], [False, False,True],
                  [False, True,False], [False, True, True],
                  [True,False,False], [True,False,True],
                  [True,True,False], [True,True, True]]
        self.assertEqual(expected, g.generuj(3))

    def testIlosciLogiki(self):
        g= GeneratorLogiki()
        self.assertEqual(16, len(g.generuj(4)))
        self.assertEqual(32, len(g.generuj(5)))
        self.assertEqual(64, len(g.generuj(6)))
            
           
class TestEwaluatora(unittest.TestCase):
    def testPorownania(self):
        ew = EwaluatorWyrazen()
        self.assertTrue(ew.porownajWyniki([False,False],[False,False]))
        self.assertTrue(ew.porownajWyniki([False,True],[False,True]))

        self.assertFalse(ew.porownajWyniki([False,True, False],[False,True]))
        self.assertFalse(ew.porownajWyniki([True,True],[False,True]))
        
    def test1(self):
        def f(a,b):
            return a==False and b == True
        wyrazenie = f
        ew = EwaluatorWyrazen()
        #true tylko dla 01, reszta false
        expected=[False, True, False, False]
        self.assertEqual(expected, ew.foo(wyrazenie, 2))


if __name__ == '__main__':
    unittest.main()
