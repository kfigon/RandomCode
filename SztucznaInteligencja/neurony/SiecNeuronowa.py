__author__ = 'kamil'
from Perceptron import *

class SiecNeuronowa:
    def __init__(self, iloscWejsc, iloscNeuronowWarstwyUkrytej, iloscWyjsc):
        self.__wyjscia = [Perceptron(iloscWejsc, Sigmoida())]*iloscWyjsc
        self.__warstwaUkryta = [Perceptron(iloscWejsc, Sigmoida())]*iloscNeuronowWarstwyUkrytej

    def zgaduj(self, inputData):
        wynikWarstwyUkrytej = []
        for p in self.__warstwaUkryta:
            wynikWarstwyUkrytej.append(p.zgaduj(inputData))

        out = []
        for p in self.__wyjscia:
            out.append(p.zgaduj(wynikWarstwyUkrytej))
        return out