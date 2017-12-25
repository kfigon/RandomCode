import unittest

class Pole:
    Puste=0
    Kolko=1
    Krzyzyk=2
    @staticmethod
    def toStr(v):
        if(v==Pole.Puste):
            return ' '
        elif(v==Pole.Kolko):
            return 'O'
        else:
            return 'X'
class Wynik:
    NiktNieWygral=0
    KrzyzykWygral=1
    KolkoWygral=2
    Remis=3
    
class Gra:
    def __init__(self):
        self.__pole = [Pole.Puste]*9
        self.__czyTerazKrzyzyk = True
        
    def __str__(self):
        out=""
        for i in range(len(self.__pole)):
            out += Pole.toStr(self.__pole[i])
            if(i%3 == 2 and i <6):
                out+="\n"
        return out
    
    def __repr__(self):
        return str(self)

    def __ruchInternal(self, idx, czyKrzyzyk):
        if(self.__pole[idx] != Pole.Puste):
            return
        doPostawienia = Pole.Kolko
        if(czyKrzyzyk):
            doPostawienia = Pole.Krzyzyk

        self.__pole[idx] = doPostawienia

    def ruch(self, idx):
        self.__ruchInternal(idx, self.__czyTerazKrzyzyk)
        self.__czyTerazKrzyzyk = not self.__czyTerazKrzyzyk
        
    def czytajPole(self, idx):
        return self.__pole[idx]

    def __czySaPustePola(self):
        for p in self.__pole:
            if(p == Pole.Puste):
                return True
        return False
    
    def czyKtosWygral(self):
        if(self.__czyWygrana(True)):
           return Wynik.KrzyzykWygral
        elif(self.__czyWygrana(False)):
             return Wynik.KolkoWygral
        elif(self.__czySaPustePola()):
             return Wynik.NiktNieWygral
        else:
             return Wynik.Remis

    #012
    #345
    #678
    def __czyWygrana(self, czyKrzyzyk):
        p = self.__pole
        f = Pole.Kolko
        if(czyKrzyzyk):
             f = Pole.Krzyzyk

        # poziomo
        if(p[0] == f and p[1] == f and p[2] == f):
             return True
        elif(p[3] == f and p[4] == f and p[5] == f):
             return True
        elif(p[6] == f and p[7] == f and p[8] == f):
             return True
        # pionowo
        elif(p[0] == f and p[3] == f and p[6] == f):
             return True
        elif(p[1] == f and p[4] == f and p[7] == f):
             return True
        elif(p[2] == f and p[5] == f and p[8] == f):
             return True
        # skos
        elif(p[0] == f and p[4] == f and p[8] == f):
             return True
        elif(p[2] == f and p[4] == f and p[6] == f):
             return True

        return False
             
class TestyGry(unittest.TestCase):
    def setUp(self):
        self.g=Gra()

    def testStrPuste(self):
        exp = "   \n   \n   "
        self.assertEqual(exp, str(self.g))
    #012
    #345
    #678
    def testStr(self):
        self.g.ruch(4)
        self.g.ruch(6)
        self.g.ruch(2)
        self.g.ruch(8)
        self.assertEqual(Pole.Krzyzyk, self.g.czytajPole(4))
        self.assertEqual(Pole.Kolko, self.g.czytajPole(6))
        self.assertEqual(Pole.Krzyzyk, self.g.czytajPole(2))
        self.assertEqual(Pole.Kolko, self.g.czytajPole(8))

        exp =  "  X\n"
        exp += " X \n"
        exp += "O O"
        self.assertEqual(exp, str(self.g))
        self.assertEqual(Wynik.NiktNieWygral, self.g.czyKtosWygral())
        
if __name__=="__main__":
    unittest.main()
