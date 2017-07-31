__author__ = 'kamil'

# odczepy podajemy w postaci [x^a, x^b, x^c...] bez x^0
# np. x^6 + x^5 + x^2 + x + 1
# [6, 5, 2, 1]
class Rejestr:
    def __init__(self, iloscRejestrow, odczepy):
        self.__iloscRejestrow = iloscRejestrow
        self.__odczepy = odczepy
        self.__stan = []

        for i in range(iloscRejestrow):
            self.__stan.append(0)

        self.__stan[0] = 1

    def ileCiagowMoznaWyliczyc(self):
        return ((2**self.__iloscRejestrow )- 1)

    def __przesun(self):
        for i in reversed(range(len(self.__stan)-1)):
            self.__stan[i+1] = self.__stan[i]

    def get(self):
        wynikXora = 0
        for odczep in self.__odczepy:
            wynikXora ^= self.__stan[odczep-1]

        ostatni = self.__stan[self.__iloscRejestrow-1]
        self.__przesun()
        self.__stan[0] = wynikXora

        return ostatni

