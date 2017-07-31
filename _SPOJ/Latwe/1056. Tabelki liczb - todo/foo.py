__author__ = 'kamil'

# todo: test 2i 3 nie dzialaja.
# dziala tylko macierz 3x3
def foo(tab):
    tab = przesunGore(tab)
    tab = przesunDol(tab)
    przesunLewo(tab)
    przesunPrawo(tab)

    ileKolumn = len(tab[0])
    ileWierwszy = len(tab)

    tab[ileWierwszy-2][0], \
    tab[1][ileKolumn-1] =   \
        tab[1][ileKolumn-1], \
        tab[ileWierwszy-2][0]

    return tab

def przesunGore(tab):
    for i in range(len(tab[0])-1):
        tab[0][i], tab[0][i+1] = tab[0][i+1], tab[0][i]

    return tab

def przesunDol(tab):
    idxDolu = len(tab)-1
    for i in range(len(tab[idxDolu])-1, 0, -1):
        tab[idxDolu][i], tab[idxDolu][i-1] = tab[idxDolu][i-1], tab[idxDolu][i]

    return tab

def przesunLewo(tab):
    tab[len(tab)-2][0], tab[len(tab)-1][0] = tab[len(tab)-1][0], tab[len(tab)-2][0]

def przesunPrawo(tab):
    tab[1][len(tab)-1], \
    tab[0][len(tab)-1] = \
            tab[0][len(tab)-1], \
            tab[1][len(tab)-1]   \

