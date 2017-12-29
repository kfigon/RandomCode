import unittest

class AAA:
    def foo(self):
        return 5
    
class BBB():
    def bar(self):
        print("o kruci!")

class CCC():
    def foobarz(self):
        return None

# -agregacja kilku klas
# -uproszczenie interfejsu do obiektow skladowych
# -agregacja wpolnego interfejsu skladowych klas i uproszczenie api
class Fasada:
    def __init__(self):
        self.__a = AAA()
        self.__b = BBB()
        self.__c = CCC()
    def daj5(self):
        return self.__a.foo()
    def piszRzecz(self):
        self.__b.bar()
    def dajNula(self):
        return self.__c.foobarz()


class TestyFasady(unittest.TestCase):
    def test(self):
        f = Fasada()
        self.assertEqual(5, f.daj5())
        self.assertEqual(None, f.dajNula())
        f.piszRzecz()
            
if __name__=='__main__':
    unittest.main()
