__author__ = 'kamil'

def selectionSort(tablica):
    tab = list(tablica)

    for i in range(len(tab)):
        najmniejszyIdx = najmniejszyIndeks(tab, i)
        tab[najmniejszyIdx],tab[i]=tab[i],tab[najmniejszyIdx]
    return tab

# zwraca indeks najmniejszego elementu
def najmniejszyIndeks(tab, startId):
    najmniejszyId = startId

    for i in range(startId+1, len(tab)):
        if(tab[najmniejszyId] > tab[i]):
            najmniejszyId = i

    return najmniejszyId