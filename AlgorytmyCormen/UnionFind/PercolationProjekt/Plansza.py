__author__ = 'kamil'
from tkinter import *
import random
import math
from AlgorytmyCormen.UnionFind.PercolationProjekt.KalkulatorWspolrzednych import *
from AlgorytmyCormen.UnionFind import QuickFind as QuickFind
from AlgorytmyCormen.UnionFind import QuickUnion as QuickUnion

class Pole:
    def __init__(self, idx, czyZamkniete):
        self.__id = idx
        self.__czyZamkniete = czyZamkniete

    def czyZamkniete(self):
        return self.__czyZamkniete

    def getId(self):
        return self.__id

class Plansza:
    # plansza(rozmiar x rozmiar)
    def __init__(self, rozmiar):
        self.__pola = [None]*(rozmiar*rozmiar)
        for i in range(len(self.__pola)):
            czyZamkniete = self.__generujCzyZamkniety()
            self.__pola[i] = Pole(i, czyZamkniete)

    def __generujCzyZamkniety(self):
        wynik = random.randint(0,9)
        progOtwartych = 4 # im wiecej, tym wiecej otwartych. Po rowno dla <0,9> -> 4
        return (wynik>progOtwartych)

    # just for tests/deterministic behavior
    def wstrzyknijTablice(self, boolTab):
        self.__pola = []
        self.__pola = [None] * len(boolTab)
        for i in range(len(self.__pola)):
            self.__pola[i] = Pole(i, boolTab[i])

    def czyJestPrzejscie(self):
        qf = QuickFind.QuickFind(self.getRozmiar()) # QuickUnion tez dziala!
        for i in range(len(self.__pola)):
            el = self.__pola[i]
            if(el.czyZamkniete()):
                continue
            sasiadyIdx = self.getSasiadujace(i)
            for si in sasiadyIdx:
                sasiad = self.__pola[si]
                if(sasiad.czyZamkniete() == False):
                    qf.union(si,i)
        gornyWiersz = range(self.getSzerokosc())
        dolnyWiersz = range((self.getWysokosc()-1)*self.getSzerokosc(),
                            self.getWysokosc()*self.getSzerokosc())

        for g in gornyWiersz:
            for d in dolnyWiersz:
                if(qf.areConnected(g,d)):
                    return True
        return False

    def getSasiadujace(self, idx):
        szerokoscPola,wysokoscPola= self.getWymiaryPlanszy()

        # klocek tutaj nie robi
        k = KalkulatorWspolrzednych(wysokoscPola, szerokoscPola,0, 0)
        idxW,idxK = k.mapTo2D(idx)

        out=[]
        gora = idx-szerokoscPola
        lewo = idx-1
        prawo = idx+1
        dol = idx + szerokoscPola
        if(gora>=0):
            out.append(gora)
        if(lewo >= (idxW*szerokoscPola)):
            out.append(lewo)
        if(prawo < ((idxW+1)*szerokoscPola)):
            out.append(prawo)
        if(dol < (szerokoscPola*wysokoscPola)):
            out.append(dol)
        return out

    def getPole(self,idx):
        return self.__pola[idx]

    def getRozmiar(self):
        return len(self.__pola)

    def getWysokosc(self):
        return int(math.sqrt(self.getRozmiar()))

    def getSzerokosc(self):
        return int(math.sqrt(self.getRozmiar()))

    # szerokosc, wysokosc
    def getWymiaryPlanszy(self):
        return self.getSzerokosc(), self.getWysokosc()

class WidokPlanszy:
    def __init__(self, root):
        self.__rozmiarPlanszy = 12
        self.__plansza = Plansza(self.__rozmiarPlanszy)

        self.__tekstLabelki = StringVar()
        self.__odswiezLablke()

        szerKlocka, wysKlocka = self.getWymiaryKlocka()
        szerokoscPola = szerKlocka*self.__rozmiarPlanszy
        wysokoscPola = wysKlocka*self.__rozmiarPlanszy + 40 # gorka na przycisk i label

        self.__buton = Button(root, text = 'resetuj', command=self.__resetuj)
        self.__plotno = Canvas(root, width = szerokoscPola, height = wysokoscPola)
        self.__label = Label(root, textvariable = self.__tekstLabelki)
        self.__plotno.pack()
        self.__label.pack()
        self.__buton.pack()

    def __odswiezLablke(self):
        tekst = "nie ma przeplywu"
        if(self.__plansza.czyJestPrzejscie()):
            tekst="jest przeplyw!"
        self.__tekstLabelki.set(tekst)

    def __resetuj(self):
        self.__plansza=Plansza(self.__rozmiarPlanszy)
        self.rysujPole()
        self.__odswiezLablke()

    # szerokosc, wysokosc
    def getWymiaryKlocka(self):
        return 30,30

    def rysujPole(self):
        self.__plotno.delete("all")
        for i in range(self.__plansza.getRozmiar()):
            x,y,dx,dy = self.mapIdxToPosition(i)
            kolor = self.mapIdxToColor(i)
            self.__plotno.create_rectangle(x,y, dx, dy, fill=kolor)

        self.__plotno.pack()

    def mapIdxToPosition(self, idx):
        szerokoscPlanszy,wysokoscPlanszy = self.__plansza.getWymiaryPlanszy()
        szerokoscKlocka, wysokoscKlocka = self.getWymiaryKlocka()

        k = KalkulatorWspolrzednych(wysokoscPlanszy, szerokoscPlanszy,
                                    wysokoscKlocka, szerokoscKlocka)
        return k.get(idx)

    def mapIdxToColor(self, idx):
        b = self.__plansza.getPole(idx).czyZamkniete()
        if(b == True):
            return 'gray'
        return 'deep sky blue'

def main():
    root = Tk()
    w = WidokPlanszy(root)
    w.rysujPole()
    root.mainloop()

if __name__ == '__main__':
    main()