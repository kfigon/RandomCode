import unittest

class GeneratorLogiki:    
    def __getBools(self,binary):
        out=[False]*len(binary)
        i = 0
        for b in binary:
            if(b=='1'):
                out[i]=True
            else:
                out[i]=False
            i+=1
        return out

    def generuj(self, ileZmiennych):
        out=[None]*(2**ileZmiennych)
        szablon = '0%db' % ileZmiennych
        
        for i in range(len(out)):
            liczba = format(i, szablon)
            out[i] = self.__getBools(liczba)
        return out

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

class EwaluatorWyrazen:
    def foo(self,wyrazenie, ileZmiennych):
        g = GeneratorLogiki()
        mozliwosciLogiczne = g.generuj(ileZmiennych)
        wyniki = []
        for i in mozliwosciLogiczne:
            w = wyrazenie(*i)
            wyniki.append(w)
        return wyniki

    def porownajWyniki(self,przed, po):
        if(len(przed) != len(po)):
            return False
        
        for i in range(len(przed)):
            if(przed[i] != po[i]):
                return False
        return True
    def piszArgumentyIWyniki(self, args, wynikA, wynikB):
        print("%r != %r dla:" %(wynikA, wynikB))
        print(args)
        print()
        
    def sprawdzWyrazenia(self, wyrA, wyrB, ileZmiennych):
        wynikiA = self.foo(wyrA, ileZmiennych)
        wynikiB = self.foo(wyrB, ileZmiennych)
        if(self.porownajWyniki(wynikiA, wynikiB)):
           print("to samo!")
        else:
            print("blad! Oto lista:\n")
            print(wynikiA)
            print(wynikiB)

            print("\nszczegolowe argumenty:")
            g = GeneratorLogiki()
            mozliwosciLogiczne = g.generuj(ileZmiennych)
            for i in range(len(wynikiA)):
                wA = wynikiA[i]
                wB = wynikiB[i]
                arg = mozliwosciLogiczne[i]
                if(wA != wB):
                    self.piszArgumentyIWyniki(arg, wA, wB)
            
           
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

# todo: move functions to Wyrazenie object (inheritance)
class Wyrazenie:
    def getFun(self):
        pass
    def __repr__(self):
        pass
    def __str__(self):
        pass

if __name__ == '__main__':
    ew = EwaluatorWyrazen()
    def foo(a,b):
        return a==False and b==True
    def bar(a,b):
        return not(a != False or b != True)
    def barzz(a,b):
        return a==True and b==False
    
    ew.sprawdzWyrazenia(foo, bar, 2)
    ew.sprawdzWyrazenia(barzz, bar, 2)

    unittest.main()
