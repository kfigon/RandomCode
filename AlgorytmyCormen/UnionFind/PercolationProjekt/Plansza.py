__author__ = 'kamil'
from tkinter import *
import random
import math
from AlgorytmyCormen.UnionFind.PercolationProjekt.KalkulatorWspolrzednych import *

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
        progOtwartych = 4 # im wiecej, tym wiecej otwartych
        return (wynik>progOtwartych)

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
        self.__plotno = Canvas(root, width = 300, height = 300)
        self.__plansza = Plansza(8)

    # szerokosc, wysokosc
    def getWymiaryKlocka(self):
        return 30,30

    def rysujPole(self):
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