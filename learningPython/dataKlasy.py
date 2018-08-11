import unittest
from dataclasses import dataclass
from dataclasses import FrozenInstanceError

# adnotacje typow sa potrzebne, ale opcjonalne, nie sprawdzane :(
# mozna dodawac normalnie metody
# automatycznie generuje str, init, repr, eq itd
@dataclass(frozen=True) # - immutability
class Dane:
    nazwa: str = ''
    liczba: int = 0
    piesel: str = 'default pies'

class Test(unittest.TestCase):
    def testDefault(self):
        d = Dane()
        self.assertEqual('',d.nazwa)
        self.assertEqual(0,d.liczba)
        self.assertEqual('default pies', d.piesel)

    def testKonsturktor(self):
        d = Dane('asd',1,'dsa')
        self.assertEqual('asd', d.nazwa)
        self.assertEqual(1, d.liczba)
        self.assertEqual('dsa', d.piesel)

    def testParametrized(self):
        d = Dane(liczba=123)
        self.assertEqual('',d.nazwa)
        self.assertEqual(123, d.liczba)
        self.assertEqual('default pies', d.piesel)

    def testImmutability(self):
        d = Dane(piesel = 'asdasd')
        def przypisanie(d):
            d.piesel = 'x'

        self.assertRaises(FrozenInstanceError, przypisanie, d)

if __name__ == '__main__':
    unittest.main()
