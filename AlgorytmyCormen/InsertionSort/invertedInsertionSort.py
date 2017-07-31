__author__ = 'kamil'

# od najwiekszego do najmniejszego
def invInsertionSort(tablica):
    tab = list(tablica)

    for i in range(1, len(tab)):
        el = tab[i]
        j = i-1
        while(j>=0 and el > tab[j]):
            tab[j],tab[j+1]=tab[j+1],tab[j]
            j-=1
    return tab