__author__ = 'kamil'


def podzielNaDziesiatkiIJednosci(liczbaWiekszaOd10):
    dziesiatki = int(liczbaWiekszaOd10/10)
    jednosci = liczbaWiekszaOd10 - dziesiatki*10

    return dziesiatki, jednosci

def iteracjaMnozenia(a, b, przeniesienie):
    wynikMnozenia = int(b) * int(a) + przeniesienie
    if (wynikMnozenia >= 10):
        przeniesienie, wynikMnozenia = podzielNaDziesiatkiIJednosci(wynikMnozenia)
    else:
        przeniesienie = 0

    return wynikMnozenia, przeniesienie


def foo(x, y):
    if(len(x) == 0 and len(y) == 0):
        return "0"

    dluzszy, krotszy = uporzadkuj(x,y)

    wynikObrotu=""
    przeniesienie=0
    for dl in reversed(dluzszy):
        for kr in reversed(krotszy):
            wynikMnozenia, przeniesienie = iteracjaMnozenia(dl, kr, przeniesienie)
            wynikObrotu = dopiszDoKoncaStringa(wynikObrotu, str(wynikMnozenia))

    if(przeniesienie != 0):
        wynikObrotu = dopiszDoKoncaStringa(wynikObrotu, str(przeniesienie))

    return wynikObrotu

def uporzadkuj(x,y):
    return x,y

def dopiszDoKoncaStringa(input, dopis):
    return dopis+input

def sumujWynikiCzastkowe(wynikiTab):
    if (len(wynikiTab) == 1):
        return wynikiTab[0]

    #for liczba in wynikiTab:
    #    for i in reversed(range(len(wynikiTab))):

