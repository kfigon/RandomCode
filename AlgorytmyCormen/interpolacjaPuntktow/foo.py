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
        return "%d,%d" %(self.__x, self.__y)

    def __eq__(self, other):
        return (self.getX() == other.getX() and
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
       
if __name__=="__main__":
    unittest.main()
    
