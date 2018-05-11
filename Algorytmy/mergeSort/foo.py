__author__ = 'kamil'

def mergeSort(tablica):
    tab = list(tablica)
    mergeSortInternal(tab)
    return tab

def mergeSortInternal(tab):
    if(len(tab) < 2):
        return
    dlugoscL = int(len(tab)/2)
    dlugoscR = len(tab)-dlugoscL

    l = [0]*dlugoscL
    r = [0]*dlugoscR
    for i in range(dlugoscL):
        l[i]=tab[i]
    for i in range(dlugoscR):
        r[i]=tab[i+dlugoscL]
    mergeSortInternal(l)
    mergeSortInternal(r)
    merguj(l,r,tab)

# bierze najmniejszy element z lewej i z prawej
# i sklada do tab
def merguj(lewa, prawa, tab):
    idPrawego=0
    idLewego=0
    for i in range(len(tab)):
        if(idLewego >= len(lewa)): # bierz reszte z prawego
            tab[i]=prawa[idPrawego]
            idPrawego+=1
        elif(idPrawego >= len(prawa)): # bierz reszte z lewego
            tab[i] = lewa[idLewego]
            idLewego+=1
        # najmniejszy z lewego
        elif(lewa[idLewego] < prawa[idPrawego]):
            tab[i] = lewa[idLewego]
            idLewego+=1
        # najmniejszy z prawego
        else:
            tab[i]=prawa[idPrawego]
            idPrawego+=1