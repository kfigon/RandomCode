__author__ = 'kamil'

def bubbleSort(tablica):
    tab = list(tablica)

    for i in range(len(tab)):
        for j in range(len(tab)-i- 1):
            if(tab[j] > tab[j+1]):
                tab[j],tab[j+1]=tab[j+1],tab[j]

    return tab

