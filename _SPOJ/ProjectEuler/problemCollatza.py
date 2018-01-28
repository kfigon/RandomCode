import unittest
#14. majac procedure jak nizej
# znajdz liczbe z zakresu 0-1000000
# dla ktorej wynikowy ciag bedzie najdluzszy
def foo(n):
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1

def analizuj(start):
    if(start < 1):
        return []
    out = []
    element = start
    out.append(element)
    while(element != 1):
        element = foo(element)
        out.append(element)
    return out

def liczElementy(start):
    if(start <1):
        return 0
    ile = 1
    element = start
    while(element != 1):
        element = foo(element)
        ile+=1
    return ile

class Testy(unittest.TestCase):
    def testFunkcjiParzyste(self):
        self.assertEqual(10, foo(20))
        self.assertEqual(19, foo(38))
        self.assertEqual(8, foo(16))
        self.assertEqual(94, foo(188))
        
    def testFunkcjiNieParzyste(self):
        self.assertEqual(64, foo(21))
        self.assertEqual(10, foo(3))
        self.assertEqual(16, foo(5))
        self.assertEqual(268, foo(89))

    def testAnalizy(self):
        exp=[13,40,20,10,5,16,8,4,2,1]
        self.assertEqual(exp, analizuj(13))
        self.assertEqual(10, liczElementy(13))


if __name__=='__main__':
    #unittest.main()

    najdluzszy = 0
    startDlaNajdluzszego=0
    #maks = 1000000
    maksy = [100,1000,10000,100000,1000000]
    for maks in maksy:
        for i in range(1,maks,2):
            wynik = liczElementy(i)
            if(wynik > najdluzszy):
                najdluzszy = wynik
                startDlaNajdluzszego=i
                
        print("najdluzszy = %d dla liczby %d" % (najdluzszy, startDlaNajdluzszego))


    
