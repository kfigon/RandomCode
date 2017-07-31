__author__ = 'kamil'
import math

def foo(tab):
    srednia = liczSrednia(tab)
    najblizszaSredniej = tab[0]
    delta = math.fabs(srednia - tab[0])

    for i in tab:
        nowaDelta = abs(srednia - i)
        if(nowaDelta < delta):
            delta = nowaDelta
            najblizszaSredniej = i

    print(tab)
    print("srednia", srednia)
    print("najblizej sredniej", najblizszaSredniej)
    print()
    return najblizszaSredniej



def liczSrednia(tab):
    suma = 0
    for i in tab:
        suma+=i
    return suma/len(tab)