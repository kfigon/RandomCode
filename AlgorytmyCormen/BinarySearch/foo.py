__author__ = 'kamil'

def foo(tablica, szukanaLiczba):
    polowa = int(len(tablica)/2)

    if(szukanaLiczba <= tablica[polowa]):
        return fooInternal(tablica, 0, polowa, szukanaLiczba)
    else:
        return fooInternal(tablica, polowa+1, len(tablica)-1, szukanaLiczba)

def fooInternal(tablica, idxStart, idxStop, szukana):
    polowaIdx = int((idxStart+idxStop)/2)

    if(idxStart == idxStop):
        return (tablica[polowaIdx] == szukana)

    if(szukana <= tablica[polowaIdx]): #idizemy w lewo
        return fooInternal(tablica, idxStart, polowaIdx, szukana)
    else:
        return fooInternal(tablica, polowaIdx+1, idxStop, szukana)
