__author__ = 'kamil'
import math

class Punkt:
    def __init__(self, litera, x, y):
        self.__x = x
        self.__y = y
        self.litera = litera
        self.odleglosc = liczOdleglosc(x, y)

def liczOdleglosc(x, y):
    return math.sqrt(x**2 + y**2)

def bar(daneWejsciowe):

    listaPunktow = []
    for x in daneWejsciowe:
        listaPunktow.append(Punkt(x[0],x[1],x[2]))

    posortowane = sortuj(listaPunktow)
    output = ""
    for index, wartosc in enumerate(posortowane):
        output += wartosc.litera
        if(index != len(posortowane) - 1):
            output+=" "

    return output

def sortuj(lista):
    for i in range(len(lista)):
        minIdx = i
        for k in range(i, len(lista)):
            if(lista[k].odleglosc < lista[minIdx].odleglosc):
                minIdx = k
        lista[i], lista[minIdx] = lista[minIdx], lista[i]

    return lista