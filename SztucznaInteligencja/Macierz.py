__author__ = 'kamil'

class Macierz:
    def __init__(self, matrix):
        self.__tab = matrix

    def getIloscKolumn(self):
        return len(self.__tab[0])
    def getIloscWierszy(self):
        return len(self.__tab)

    def get(self, w, k):
        return self.__tab[w][k]
    def __sprawdzRozmiary(self, macierz):
        return (self.getIloscKolumn() != macierz.getIloscKolumn() or
           self.getIloscWierszy() != macierz.getIloscWierszy())

    def dodaj(self, macierz):
        if(self.__sprawdzRozmiary(macierz)):
            raise Exception("invalid sizes")

        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                self.__tab[w][k] += macierz.get(w,k)

    def odejmij(self, macierz):
        if(self.__sprawdzRozmiary(macierz)):
            raise Exception("invalid sizes")

        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                self.__tab[w][k] -= macierz.get(w,k)

    def mnoz(self, skalar):
        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                self.__tab[w][k] *= skalar

    def mnozeMacierzeElementPoElemencie(self, macierz):
        if(self.__sprawdzRozmiary(macierz)):
            raise Exception("invalid sizes")

        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                self.__tab[w][k] *= macierz.get(w,k)

    def mnozMacierze(self, macierz):
        Aw = self.getIloscWierszy()
        Ak = self.getIloscKolumn()
        Bw = macierz.getIloscWierszy()
        Bk = macierz.getIloscKolumn()

        if(Macierz.czyMoznaMnozycMacierze(Aw,Ak,Bw,Bk) == False):
            raise Exception("invalid sizes")

        Cw, Ck = Macierz.rozmiaryPoWymnozeniu(Aw,Ak,Bw,Bk)
        tab= [[0 for j in range(Ck)] for i in range(Cw)]

        for w in range(Cw):
            for k in range(Ck):
                tab[w][k] = 0
                # suma
                for i in range(Ak):
                    a = self.get(w,i)
                    b = macierz.get(i,k)
                    tab[w][k] +=a*b

        return Macierz(tab)

    def czyMoznaMnozycMacierze(Aw, Ak,Bw, Bk):
        if(Ak == Bw):
            return True
        return False

    def rozmiaryPoWymnozeniu(Aw,Ak,Bw,Bk):
        return Aw,Bk

    def transponuj(self):
        outW = self.getIloscKolumn()
        outK = self.getIloscWierszy()
        tab = [[0 for j in range(outK)] for i in range(outW)]

        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                tab[k][w] = self.get(w,k)

        return Macierz(tab)