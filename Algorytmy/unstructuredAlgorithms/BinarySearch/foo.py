__author__ = 'kamil'

# rekurencyjnie
def binSearch(tab, x):
    return binSearchInternal(tab, x, 0, len(tab)-1)

def binSearchInternal(tab, x, startId, stopId):
    idSrodka = int((startId+stopId)/2)

    if(idSrodka == startId):
        return (tab[idSrodka] == x)

    if(x < tab[idSrodka]):
        return binSearchInternal(tab, x, startId, idSrodka)
    else:
        return binSearchInternal(tab, x, idSrodka, stopId)

# iteracyjnie
def binSearchX(tab, x):
    startId = 0
    stopId = len(tab)-1
    while(stopId - startId != 1):
        idSrodka = int((stopId+startId)/2)
        if(x<tab[idSrodka]):
            stopId = idSrodka
        else:
            startId = idSrodka

    return (tab[startId] == x)