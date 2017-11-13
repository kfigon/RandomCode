__author__ = 'kamil'
import random

def generujDane(ile, funkcjaLiniowa):
    outTab=[]
    for i in range(ile):
        x = random.randint(-50,50)
        y = random.randint(-100,100)
        klasa = 1
        if(y < funkcjaLiniowa.get(x)):
            klasa = -1
        ptk = {'x':x,'y':y,'klasa':klasa}
        outTab.append(ptk)
    return outTab

# tylko 2!
def toInput(krotka):
    dl = len(krotka)-1 # bo klasa na koncu
    assert dl == 2

    return [krotka['x'], krotka['y']]

# procent bledow
def sprawdzIleBledow(mozg, dane):
    ileBledow = 0
    for d in dane:
        predykcja = mozg.zgaduj(toInput(d))
        if(predykcja != d['klasa']):
            ileBledow +=1

    return ileBledow/len(dane)*100

def trening(mozg, dane):
    for d in dane:
        mozg.trenuj(toInput(d), d['klasa'])

