class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def konwersjaIntPunkt(listaArgumentow):
    listaPunktow = []
    for i in range(0, len(listaArgumentow), 2):
        punkt = Punkt(listaArgumentow[i], listaArgumentow[i+1])
        listaPunktow.append(punkt)

    return listaPunktow

def liczPole(listaPunktow):
    suma = 0
    for index in range(len(listaPunktow)):
        if(index == 0):
            indexLow = len(listaPunktow)-1
            indexHigh = index + 1

        elif(index == len(listaPunktow) - 1):
            indexLow = index - 1
            indexHigh = 0

        else:
            indexLow = index-1
            indexHigh = index +1

        suma += (listaPunktow[indexLow].y - listaPunktow[indexHigh].y)*listaPunktow[index].x

    return suma/2

def liczWszystko(listaCzarnych, listaSzarych):
    if len(listaCzarnych) % 2 !=0 or len(listaSzarych) % 2 != 0:
        raise Exception('nieparzysta ilosc arg: czarne: ' +
                        str(len(listaCzarnych))+ ", szare: " +
                        str(len(listaSzarych)))


    poleCzarnych = liczPole(konwersjaIntPunkt(listaCzarnych))
    poleSzarych = liczPole(konwersjaIntPunkt(listaSzarych))
    return abs(poleSzarych*6 + poleCzarnych*10 - poleCzarnych*6)