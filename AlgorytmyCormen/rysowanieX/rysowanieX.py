import unittest

class Output:
    def __init__(self):
        self.__nap = ""

    def czysc(self):
        self.__nap=""

    def __dopiszSpacje(self, ile):
        for s in range(ile):
            self.__nap+=' '

    def __kropka(self):
        self.__nap += '*'
        
    def draw(self, rozmiarIksa):
        k = KalkulatorSpacji(rozmiarIksa)
        czyParzystyRozmiar = (rozmiarIksa % 2) == 0
        
        for wiersz in range(rozmiarIksa):
            spacjeZew, spacjeWew = k.licz(wiersz)
        
            self.__dopiszSpacje(spacjeZew)
            self.__kropka()
            
            self.__dopiszSpacje(spacjeWew)
            # dla nieparzystych jedna kropka
            if(spacjeWew != 0 and czyParzystyRozmiar == False):
                self.__kropka()
            # dla parzystych beda 2 kropki, bez spacji pomiedzy
            elif(czyParzystyRozmiar):
                self.__kropka()

            self.__dopiszSpacje(spacjeZew)
            self.__nap+='\n'
            
    def __str__(self):
        return self.__nap

    def __repr__(self):
        return str(self)

class Test(unittest.TestCase):
    def setUp(self):
        self.o = Output()
        
    def testEmpty(self):
        self.assertEqual("", str(self.o))

    def testDraw5(self):
        self.o.draw(5)
        exp = '*   *\n'
        exp +=' * * \n'
        exp +='  *  \n'
        exp +=' * * \n'
        exp +='*   *\n'
        self.assertEqual(exp, str(self.o))

    def testDraw7(self):
        self.o.draw(7)
        exp = '*     *\n'
        exp +=' *   * \n'
        exp +='  * *  \n'
        exp +='   *   \n'
        exp +='  * *  \n'
        exp +=' *   * \n'
        exp +='*     *\n'
        self.assertEqual(exp, str(self.o))
    def testDraw6(self):
        self.o.draw(6)
        exp = '*    *\n'
        exp +=' *  * \n'
        exp +='  **  \n'
        exp +='  **  \n'
        exp +=' *  * \n'
        exp +='*    *\n'
        self.assertEqual(exp, str(self.o))
        
    def testCzysc(self):
        self.o.draw(3)
        self.o.czysc()
        self.assertEqual("", str(self.o))
        

class KalkulatorSpacji:
    def __init__(self, rozmiar):
        self.__rozmiar = rozmiar

    def licz(self, wiersz):
        srodek = self.__rozmiar//2

        zew = wiersz
        if(wiersz >= srodek):
            zew = self.__rozmiar - wiersz -1
            
        wew = self.__rozmiar - 2*zew-2
        if(wew <0):
            wew =0
        return zew,wew
    
class TestyKalkulatora(unittest.TestCase):
    def test5(self):
        k = KalkulatorSpacji(5)
        self.assertEqual((0,3), k.licz(0))
        self.assertEqual((1,1), k.licz(1))
        self.assertEqual((2,0), k.licz(2))
        self.assertEqual((1,1), k.licz(3))
        self.assertEqual((0,3), k.licz(4))

    def test7(self):
        k = KalkulatorSpacji(7)
        self.assertEqual((0,5), k.licz(0))
        self.assertEqual((1,3), k.licz(1))
        self.assertEqual((2,1), k.licz(2))
        self.assertEqual((3,0), k.licz(3))
        self.assertEqual((2,1), k.licz(4))
        self.assertEqual((1,3), k.licz(5))
        self.assertEqual((0,5), k.licz(6))

    def test6(self):
        k = KalkulatorSpacji(6)
        self.assertEqual((0,4), k.licz(0))
        self.assertEqual((1,2), k.licz(1))
        self.assertEqual((2,0), k.licz(2))
        self.assertEqual((2,0), k.licz(3))
        self.assertEqual((1,2), k.licz(4))
        self.assertEqual((0,4), k.licz(5))

if __name__ == "__main__":
    unittest.main()
