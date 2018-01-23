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

    def __kopiujTab(self):
        tab = self.__getEmptyTab(self.getIloscWierszy(), self.getIloscKolumn())
        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                tab[w][k] = self.__tab[w][k]
        return tab

    def __getEmptyTab(self, w, k):
        return [[0 for j in range(k)] for i in range(w)]

    def __sprawdzRozmiary(self, macierz):
        return (self.getIloscKolumn() != macierz.getIloscKolumn() or
           self.getIloscWierszy() != macierz.getIloscWierszy())

    def dodaj(self, macierz):
        if(self.__sprawdzRozmiary(macierz)):
            raise Exception("invalid sizes")

        tab = self.__kopiujTab()
        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                tab[w][k] = self.get(w,k) + macierz.get(w,k)
        return Macierz(tab)

    def odejmij(self, macierz):
        if(self.__sprawdzRozmiary(macierz)):
            raise Exception("invalid sizes")

        tab = self.__kopiujTab()
        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                tab[w][k] = self.get(w,k) - macierz.get(w,k)
        return Macierz(tab)

    def mnoz(self, skalar):
        tab = self.__kopiujTab()
        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                tab[w][k] *= skalar
        return Macierz(tab)

    def dodajSkalar(self, skalar):
        tab = self.__kopiujTab()
        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                tab[w][k] += skalar
        return Macierz(tab)

    def odejmijSkalar(self, skalar):
        tab = self.__kopiujTab()
        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                tab[w][k] -= skalar
        return Macierz(tab)

    def mnozeMacierzeElementPoElemencie(self, macierz):
        if(self.__sprawdzRozmiary(macierz)):
            raise Exception("invalid sizes")
        tab = self.__kopiujTab()
        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                tab[w][k] = self.get(w,k) * macierz.get(w,k)
        return Macierz(tab)

    def mnozMacierze(self, macierz):
        Aw = self.getIloscWierszy()
        Ak = self.getIloscKolumn()
        Bw = macierz.getIloscWierszy()
        Bk = macierz.getIloscKolumn()

        if(Macierz.czyMoznaMnozycMacierze(Aw,Ak,Bw,Bk) == False):
            raise Exception("invalid sizes")

        Cw, Ck = Macierz.rozmiaryPoWymnozeniu(Aw,Ak,Bw,Bk)
        tab = self.__getEmptyTab(Ck, Cw)

        for w in range(Cw):
            for k in range(Ck):
                tab[w][k] = 0
                # suma
                for i in range(Ak):
                    a = self.get(w,i)
                    b = macierz.get(i,k)
                    tab[w][k] += a*b

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

    def __str__(self):
        out = ""
        for w in range(self.getIloscWierszy()):
            for k in range(self.getIloscKolumn()):
                out += str(self.get(w,k))
                if(k != self.getIloscKolumn()-1):
                    out+=" "
            if(w != self.getIloscWierszy() -1):
                out+="\n"
        return out
    
    def __repr__(self):
        return str(self)