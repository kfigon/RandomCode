__author__ = 'kamil'
from random import shuffle

# to wszystko. Do kontrolera i view i wsio

class Element:
    def __init__(self, id):
        self.__id = id
        self.__zgadniete = False
    def getId(self):
        return self.__id
    def czyZgadniety(self):
        return self.__zgadniete
    def setZgadniete(self):
        self.__zgadniete = True

class Game:
    def __init__(self, ilePol):
        self.__board = Board(ilePol)

    def getBoardElement(self, index):
        return self.__board.getData()[index]
    def getBoard(self):
        return self.__board

    def czyWszystkieZgadniete(self):
        for i in range(self.getBoard().getSize()):
            el = self.getBoardElement(i)
            if(el.czyZgadniety() == False):
                return False
        return True

    def zgadnij(self, numer1, numer2):
        a = self.getBoardElement(numer1)
        b = self.getBoardElement(numer2)
        if(a.getId() == b.getId()):
            a.setZgadniete()
            b.setZgadniete()
            return True
        return False

class Board:
    def __init__(self, ilePol):
        assert(ilePol % 2 == 0)
        self.__tab = [None for i in range(ilePol)]

        randomList = self.generateRandomList(ilePol)
        id = 0
        for i in range(len(randomList)):
            if(i!=0 and i%2 == 0):
                id+=1
            self.__tab[randomList[i]] = Element(id)

    # generujemy liste losowych numerow i
    # na sasiadujacych wsadzamy te same ID
    def generateRandomList(self, ile):
        x = [i for i in range(ile)]
        shuffle(x)
        return x

    def getData(self):
        return self.__tab

    def getSize(self):
        return len(self.__tab)

    # uzywany tylko do testow, przyjmuje tablice Elementow
    def injectBoard(self, tab):
        self.__tab.clear()
        self.__tab = list(tab)