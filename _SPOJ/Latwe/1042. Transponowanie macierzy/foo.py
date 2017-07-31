__author__ = 'kamil'

class Macierz:
    def __init__(self, macierz):
        self.macierz = macierz
        self.ileKolumn = len(macierz[0])
        self.ileWierwszy = len(macierz)

    def transponuj(self):
        macierzOut = [[] for i in range(self.ileKolumn)]

        for w in range(self.ileWierwszy):
            for k in range(self.ileKolumn):
                macierzOut[k].append(self.macierz[w][k])

        return Macierz(macierzOut)

def foo(macierz):
    macierzIn = Macierz(macierz)
    return macierzIn.transponuj().macierz