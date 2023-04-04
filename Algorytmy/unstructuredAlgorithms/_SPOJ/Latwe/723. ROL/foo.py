__author__ = 'kamil'

def foo(tab):
    for i in range(len(tab)-1):
        # zawiniecie
        if(i==0):
            tab[i],tab[len(tab)-1] = tab[len(tab)-1], tab[i]
        # reszta
        else:
            tab[i-1],tab[i] = tab[i],tab[i-1]

    return tab