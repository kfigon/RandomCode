__author__ = 'kamil'
from SztucznaInteligencja.Funkcje import *

class Perceptron:
    def __init__(self, ileWejsc=2, funkcjaAktywacji = Signum()):
        self.__wagi = [1]*ileWejsc
        self.__stala = 1    #bias
        self.__funkcjaAktywacji = funkcjaAktywacji

    def zgaduj(self, inputData):
        suma=self.__stala
        for i in range(len(self.__wagi)):
            suma += self.__wagi[i]*inputData[i]

        return self.__funkcjaAktywacji.get(suma)

    def __liczBlad(self, expeced, predykcja):
        return expeced-predykcja

    # jeden przypadek
    def trenuj(self, inputData, wynik):
        predykcja = self.zgaduj(inputData)
        blad = self.__liczBlad(wynik, predykcja)
        learningStep=0.1
        for i in range(len(self.__wagi)):
            self.__wagi[i] += blad*learningStep*inputData[i]
        self.__stala += blad*3 # jakos tak lepiej

    def __str__(self):
        napis = ""
        i=0
        for w in self.__wagi:
            napis += ("w%d: %d, " % (i, w))
            i+=1
        napis += "bias: " + str(self.__stala)
        return napis

    def getFunkcjaLiniowa(self):
        a = -self.__stala/self.__wagi[1]
        b = -self.__wagi[0]/self.__wagi[1]
        return FunkcjaLiniowa(a,b)