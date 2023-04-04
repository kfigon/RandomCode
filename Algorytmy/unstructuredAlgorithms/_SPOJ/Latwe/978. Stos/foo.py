__author__ = 'kamil'

class Stos:
    def __init__(self):
        self.__tab = [0]*10
        self.__wierzcholek = 0

    def __getRozmiarStosu(self):
        return len(self.__tab)

    def push(self, liczba):
        if(self.__wierzcholek >= self.__getRozmiarStosu()):
            return False
        self.__tab[self.__wierzcholek] = liczba
        self.__wierzcholek += 1
        return True

    def pop(self):
        if(self.__wierzcholek <= 0):
            return False
        self.__wierzcholek -= 1
        return self.__tab[self.__wierzcholek]


