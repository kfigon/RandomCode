import unittest

class DFS:
    def __init__(self, graf):
        self.__g=graf
        self.__listaOdwiedzonych = []
        # -1 -> brak polaczenia
        self.__listaPolaczen = []
        self.__czysc()
        
    def __czysc(self):
        self.__listaOdwiedzonych=[False]*self.__g.getIloscWezlow()
        self.__listaPolaczen=[-1]*self.__g.getIloscWezlow()
        
    def walk(self, start, stop):
        self.__czysc()
        self.__odwiedz(start)
        
        droga=[] # indeksy po kolei do odwiedzenia celu

        i=stop
        while(i != -1):
            droga.append(i)
            i = self.__listaPolaczen[i]
                
        return list(reversed(droga))

    def czyPolaczone(self, start,stop):
        droga = self.walk(start,stop)
        return len(droga) != 0

    def __odwiedz(self, wezelId):
        asdasd = self.__listaPolaczen
        sad = self.__listaOdwiedzonych

        if(self.__czyOdwiedzony(wezelId)):
            return
        self.__listaOdwiedzonych[wezelId] = True
        sasiady = self.__g.getListaSasiadow(wezelId)
        for i in sasiady:
            if(self.__czyOdwiedzony(i)):
                continue
            self.__listaPolaczen[i]=wezelId
            self.__odwiedz(i)
            
    def __czyOdwiedzony(self, wezelId):
        return self.__listaOdwiedzonych[wezelId]        
        
class Graf:
    def __init__(self, ileElementow):
        self.__tab=[None]*ileElementow
        for i in range(ileElementow):
            self.__tab[i] = [False]*ileElementow

    def getListaSasiadow(self, idx):
        out=[]
        for x in range(self.getIloscWezlow()):
            if(x is not idx and self.czyPolaczone(idx, x)):
               out.append(x)
        return out
    
    def polacz(self, v,w):
        self.__tab[v][w]=True
        self.__tab[w][v]=True

    def czyPolaczone(self,v,w):
        return self.__tab[v][w]
        
    def getIloscWezlow(self):
        return len(self.__tab) #NxN, wiec zadziala

    # todo
    def getIloscSciezek(self):
        return 0

    
    # todo make it more readabile
    # wszystkie polaczenia ladnie wyswietlone
    # nie powatarzaja sie
    def __str__(self):
        return str(self.__tab)

    # macierz polaczen
    def __repr__(self):
        return str(self.__tab)

class TestyGrafu(unittest.TestCase):
    def testEmptyGraf(self):
        g = Graf(3)
        expected = [[False,False,False],
                    [False,False,False],
                    [False,False,False]]
        self.assertEqual(str(expected),repr(g))
        self.assertEqual(3, g.getIloscWezlow())
        self.assertEqual(0, g.getIloscSciezek())
        
    def testAddConnection(self):
        g=Graf(3)
        g.polacz(2,1)
        self.assertTrue(g.czyPolaczone(2,1))
        self.assertTrue(g.czyPolaczone(1,2))
        expected = [[False,False,False],
                    [False,False,True],
                    [False,True,False]]
        self.assertEqual(str(expected), repr(g))
        self.assertEqual(3, g.getIloscWezlow())
        #self.assertEqual(1, g.getIloscSciezek())
        
        self.assertFalse(g.czyPolaczone(0,0))
        self.assertFalse(g.czyPolaczone(2,2))
        self.assertFalse(g.czyPolaczone(0,1))
        self.assertFalse(g.czyPolaczone(0,2))

    def testSasiadowBezPolaczen(self):
        g = Graf(3)
        self.assertEqual([], g.getListaSasiadow(0))
        self.assertEqual([], g.getListaSasiadow(1))
        self.assertEqual([], g.getListaSasiadow(2))

    def testSasiadow(self):
        g=Graf(3)
        g.polacz(0,1)
        self.assertEqual([1], g.getListaSasiadow(0))
        self.assertEqual([0], g.getListaSasiadow(1))
        self.assertEqual([], g.getListaSasiadow(2))

    #0-1 2 3
    #  |   |
    #4 5-6-7
    def testSasiadow2(self):
        g=Graf(8)
        g.polacz(0,1)
        g.polacz(1,5)
        g.polacz(7,6)
        g.polacz(5,6)
        g.polacz(7,3)

        self.assertEqual([1],   g.getListaSasiadow(0))
        self.assertEqual([0,5], g.getListaSasiadow(1))
        self.assertEqual([],    g.getListaSasiadow(2))
        self.assertEqual([7],   g.getListaSasiadow(3))
        self.assertEqual([],   g.getListaSasiadow(4))
        self.assertEqual([1,6],    g.getListaSasiadow(5))
        self.assertEqual([5,7],   g.getListaSasiadow(6))
        self.assertEqual([3,6],   g.getListaSasiadow(7))
        
    @unittest.skip("todo toString")
    def testyToStringEmpty(self):
        g = Graf(3)
        self.assertEqual("", str(g))

    @unittest.skip("todo toString")
    def testyToString(self):
        g=Graf(3)
        g.polacz(1,2)
        self.assertEqual("1-2", str(g))

class TestyDFS(unittest.TestCase):
    #0-1 2 3
    #  |   |
    #4 5-6-7
    def testyChodzenia(self):
        g=Graf(8)
        g.polacz(0,1)
        g.polacz(1,5)
        g.polacz(7,6)
        g.polacz(5,6)
        g.polacz(7,3)

        dfs = DFS(g)
        self.assertEqual([0,1,5,6,7,3], dfs.walk(0,3))
        self.assertTrue(dfs.czyPolaczone(0,3))

    def testyChodzenia2(self):
        g=Graf(13)
        g.polacz(0,1)
        g.polacz(2,0)
        g.polacz(4,6)
        g.polacz(0,6)
        g.polacz(3,4)
        g.polacz(3,5)
        g.polacz(4,5)

        g.polacz(7,8)
        g.polacz(9,10)
        g.polacz(9,11)
        g.polacz(12,9)

        dfs = DFS(g)
        self.assertEqual([0,6,4,3], dfs.walk(0,3))
        self.assertEqual([7,8], dfs.walk(7,8))
        self.assertEqual([9,10], dfs.walk(9,10))
        self.assertEqual([9,11], dfs.walk(9,11))
        self.assertEqual([11,9,12], dfs.walk(11,12))

    def testCzyPolaczone(self):
        g=Graf(3)
        g.polacz(2,1)
        
        dfs = DFS(g)
        self.assertTrue(dfs.czyPolaczone(2,1))
        self.assertTrue(dfs.czyPolaczone(1,2))         
        
if __name__=='__main__':
    unittest.main()
