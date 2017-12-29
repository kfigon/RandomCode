import unittest

class Klient: 
    def foo(self):
        return 555

class Serwis:
    def uzywaj(self, napisele):        
        if(napisele == '555'):
            return '123'
        return None

# konwersja jednego API do drugiego
# wrapuje zasob na cos, z czym klient potrafi gadac
# klient ma liczby, a serwis uzywa napisow. Jakas konwersja wymagana
# konwersja moze byc dwustronna (input i output przerabiane)

# mozna tez dodac adapter do klienta:
# klient ma adapter i zasob, adapter ma zasob, klient wola adapter
# adapter odpowiada za translacje w 2 strony
class Adapter:
    def __init__(self, zasob):
        self.z = zasob
        
    def robRzeczy(self, daneKlienta):
        danePoKonwersji = str(daneKlienta)
        wynik = self.z.uzywaj(danePoKonwersji)
        return int(wynik)
    

    
class TestyAdaptera(unittest.TestCase):
    def testBezAdaptera(self):
        k = Klient()
        dane = k.foo()
        serwis = Serwis()        
        self.assertEqual(None, serwis.uzywaj(dane))

    def testSerwisu(self):
        serwis = Serwis()
        self.assertEqual('123', serwis.uzywaj('555'))
        
    def test(self):
        k = Klient()
        dane = k.foo()
        serwis = Serwis()

        adapter = Adapter(serwis)
        self.assertEqual(123, adapter.robRzeczy(dane))                 

if __name__=='__main__':
    unittest.main()
