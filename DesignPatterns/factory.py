import unittest

class Baza:
    def fun(self):
        return 5
    
class Pochodna(Baza):
    def fun(self):
        return 12

class Pochodniejsza(Baza):
    def fun(self):
        return 9999123


# klasa fabrykujaca pozwala grupowac metody
# fabrykujace przy wiekszej ilosci klas
def fabryka(napis):
    if(napis == 'baza'):
        return Baza()
    elif(napis == 'poch'):
        return Pochodna()
    elif(napis == 'poch2'):
        return Pochodniejsza()
    
    return None

class TestyFabryki(unittest.TestCase):
    def testBaza(self):
        baz = fabryka('baza')
        self.assertEqual(Baza, type(baz))
        self.assertNotEqual(Pochodna, type(baz))
        self.assertNotEqual(Pochodniejsza, type(baz))
    def testPochodna(self):
        o = fabryka('poch')
        self.assertNotEqual(Baza, type(o))
        self.assertEqual(Pochodna, type(o))
        self.assertNotEqual(Pochodniejsza, type(o))
    def testPochodniejsza(self):
        o = fabryka('poch2')
        self.assertNotEqual(Baza, type(o))
        self.assertNotEqual(Pochodna, type(o))
        self.assertEqual(Pochodniejsza, type(o))
            
if __name__=='__main__':
    unittest.main()
