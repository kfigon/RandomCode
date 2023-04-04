__author__ = 'kamil'
def foo(listaObzartuchow, iloscCiastekWPudelku):
    dobaWSekundach = 60*60*24
    ileTrzebaCiastek = 0
    for obzartuch in listaObzartuchow:
        ileTrzebaCiastek += int(dobaWSekundach/obzartuch)

    ilePudelek=1
    while(ilePudelek * iloscCiastekWPudelku < ileTrzebaCiastek):
        ilePudelek+=1

    return ilePudelek