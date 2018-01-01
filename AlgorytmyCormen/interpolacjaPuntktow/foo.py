import unittest

class Punkt:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    
    def __repr__(self):
        return str(self)
    def __str__(self):
        if(self == None):
            return "None"
        return "%d,%d" %(self.__x, self.__y)

    def __eq__(self, other):
        return (other != None and
                self.getX() == other.getX() and
                self.getY() == other.getY())

class TesyPunktu(unittest.TestCase):
    def test1(self):
        p = Punkt(1,2)
        self.assertEqual(1, p.getX())
        self.assertEqual(2, p.getY())
        self.assertEqual("1,2", str(p))
        
    def testEq(self):
        p1 = Punkt(1,2)
        p2 = Punkt(2,3)
        self.assertNotEqual(p1,p2)
        self.assertTrue(p1 == Punkt(1,2))
        self.assertEqual(p1, Punkt(1,2))

def wyznaczWspolczynniki(p1, p2):
    x1 = p1.getX()
    x2= p2.getX()
    y1=p1.getY()
    y2=p2.getY()
    w = x1-x2
    wa = y1-y2
    wb=x1*y2 - y1*x2
    return (wa/w, wb/w)

class TestyFunkcjiLiniowej(unittest.TestCase):
    def testFunkcji(self):
        a,b = wyznaczWspolczynniki(Punkt(1,2), Punkt(3,5))
        self.assertEqual(3/2, a)
        self.assertEqual(1/2, b)

def tworzKierunek(p1,p2):
    a,b = wyznaczWspolczynniki(p1,p2)
    
    doGory = a > 0
    zLewaNaPrawo = (p1.getX() < p2.getX())

    if(doGory and zLewaNaPrawo):
        return range(p1.getX(), p2.getX()+1)
    elif(zLewaNaPrawo and doGory==False):
        return range(p1.getX(), p2.getX()+1)
    elif(zLewaNaPrawo==False and doGory):
        return range(p1.getX(), p2.getX()-1, -1)
    else:
        return range(p1.getX(), p2.getX()-1, -1)
        
def interpoluj(start, stop):
    if(start == stop):
        return [start,stop]

    out=[]
    # przypadek 'niepionowy'
    if(start.getX() != stop.getX()):
        a,b = wyznaczWspolczynniki(start,stop)
        zbior = tworzKierunek(start,stop)
        for x in zbior:
            y=round(a*x+b)
            out.append(Punkt(x,y))
    # pionowy
    else:
        zDoluDoGory = start.getY() < stop.getY()
        zbior=None
        if(zDoluDoGory):
            zbior = range(start.getY(), stop.getY()+1)
        else:
            zbior = range(start.getY(), stop.getY()-1,-1)
        for y in zbior:
            out.append(Punkt(start.getX(), y))
        
    return out

class TestInterpolacji(unittest.TestCase):
    def testLewoPrawoGora(self):
        p1 = Punkt(1,2)
        p2 = Punkt(3,5)
        self.assertEqual([p1, Punkt(2,4), p2], interpoluj(p1,p2))
    def testPrawoLewoDol(self):
        p2 = Punkt(1,2)
        p1 = Punkt(3,5)
        self.assertEqual([p1, Punkt(2,4), p2], interpoluj(p1,p2))
    def testLewoPrawoGora2(self):
        self.assertEqual([Punkt(1,1),Punkt(2,2), Punkt(3,3),Punkt(4,4),
                          Punkt(5,5)], interpoluj(Punkt(1,1), Punkt(5,5)))
    def testLewoPrawoDol(self):
       exp=[Punkt(1,5),Punkt(2,4),Punkt(3,3),Punkt(4,2),Punkt(5,1)]
       self.assertEqual(exp, interpoluj(Punkt(1,5), Punkt(5,1)))

    def testPrawoLewoGora(self):
       exp=[Punkt(6,1),Punkt(5,2),Punkt(4,3),Punkt(3,4),Punkt(2,5),Punkt(1,6)]
       self.assertEqual(exp, interpoluj(Punkt(6,1), Punkt(1,6)))
    
    def testPionowoDoGory(self):
        exp=[Punkt(2,3),Punkt(2,4),Punkt(2,5),Punkt(2,6)]
        self.assertEqual(exp, interpoluj(Punkt(2,3), Punkt(2,6)))
    def testPionowoDoDolu(self):
        exp=[Punkt(2,6),Punkt(2,5),Punkt(2,4),Punkt(2,3),Punkt(2,2),Punkt(2,1)]
        self.assertEqual(exp, interpoluj(Punkt(2,6), Punkt(2,1)))


class WalidatorPozycjiPunktu:
    def __init__(self, ksztalt):
        self.__k = ksztalt

    def czyWewnatrz(self, punkt):
        gora = None
        dol = None
        lewo = None
        prawo = None

        # maksy/min wybierac!
        for p in self.__k:
            if(p.getX() == punkt.getX()):
                if(gora == None or gora.getY() <= p.getY()):
                    gora = p
                if(dol == None or dol.getY() >= p.getY()):
                    dol = p
            if(p.getY() == punkt.getY()):
                if(lewo == None or lewo.getX() >= p.getX()):
                    lewo = p
                if(prawo == None or prawo.getX() <= p.getX()):
                    prawo = p
        
        #print("\n%s -> %s, %s, %s, %s" % (str(punkt), str(gora), str(dol), str(lewo), str(prawo)))
        if(gora == None or dol == None or lewo == None or prawo == None):
            return False
        
        if(punkt.getY() <= gora.getY() and
           punkt.getY() >= dol.getY() and
           punkt.getX() >= lewo.getX() and
           punkt.getX() <= prawo.getX()):
            return True
        
        return False

class TestyWnetrza(unittest.TestCase):
    def setUp(self):
        k = [Punkt(3,8), Punkt(4,7),Punkt(5,7),Punkt(6,6),
                  Punkt(7,5),Punkt(7,4),Punkt(7,3),Punkt(6,3),
                  Punkt(5,3),Punkt(4,3),Punkt(3,3),Punkt(3,4),
                  Punkt(3,5),Punkt(3,6),Punkt(3,7),Punkt(3,8)]

        self.w = WalidatorPozycjiPunktu(k)

    def test44(self):
        p = Punkt(4,4)
        self.assertTrue(self.w.czyWewnatrz(p))
    def test33(self):
        p = Punkt(3,3)
        self.assertTrue(self.w.czyWewnatrz(p))
    def test43(self):
        p = Punkt(4,3)
        self.assertTrue(self.w.czyWewnatrz(p))
    def test64(self):
        p = Punkt(6,4)
        self.assertTrue(self.w.czyWewnatrz(p))
    def test47(self):
        p = Punkt(4,7)
        self.assertTrue(self.w.czyWewnatrz(p))
    def test26(self):
        p = Punkt(2,6)
        self.assertFalse(self.w.czyWewnatrz(p))

        
if __name__=="__main__":
    unittest.main()
    
