__author__ = 'kamil'

def insertionSort(input):
    tab = list(input)
    for i in range(1, len(tab)):
        j = i-1
        element = tab[i]
        while(j>=0 and tab[j] > element):
            tab[j+1],tab[j] = tab[j],tab[j+1]
            j-=1
    return tab