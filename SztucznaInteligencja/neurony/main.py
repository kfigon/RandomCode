__author__ = 'kamil'
import random
from Funkcje import FunkcjaLiniowa
from Perceptron import *
from tkinter import *

def generujDane(ile, funkcjaLiniowa):
    outTab=[]
    for i in range(ile):
        x = random.randint(0,300)
        y = random.randint(0,300)
        klasa = 1
        if(y < funkcjaLiniowa.get(x)):
            klasa = -1
        ptk = {'x':x,'y':y,'klasa':klasa}
        outTab.append(ptk)
    return outTab

# tylko 2!
def toVector(krotka):
    dl = len(krotka)-1 # bo klasa na koncu
    assert dl == 2

    return [krotka['x'], krotka['y']]

# procent bledow
def sprawdzIleBledow(mozg, dane):
    ileBledow = 0
    for d in dane:
        predykcja = mozg.zgaduj(toVector(d))
        if(predykcja != d['klasa']):
            ileBledow +=1

    return ileBledow/len(dane)*100

def trening(mozg, dane):
    for d in dane:
        mozg.trenuj(toVector(d), d['klasa'])

def main():
    f = FunkcjaLiniowa(random.randint(0,10), random.randint(0,100))
    # todo: to nie dziala!
    #f = FunkcjaLiniowa(0, 100)
    dane = generujDane(5000, f)
    mozg = Perceptron()
    trening(mozg, dane)
    procentBledow = sprawdzIleBledow(mozg, dane)

    print("ideal\t" + str(f))
    print("wynik\t" + str(mozg.getFunkcjaLiniowa()))
    print("procent bledow: %f%%" % (procentBledow))
    print("perceptron: " + str(mozg))
    wizualizujDane(generujDane(100, f), f, mozg.getFunkcjaLiniowa())

def wizualizujDane(dane, idealnaLinia, otrzymanaLinia):
    okno = Tk()
    pole = Canvas(okno, width=300, height=300)
    for d in dane:
        x=d['x']
        y=d['y']
        kolor = 'blue'
        if(d['klasa'] >0):
            kolor='red'
        pole.create_oval(x,y, x+5, y+5, fill=kolor)

    pole.create_line(0, idealnaLinia.get(0), 300, idealnaLinia.get(300), width=2, fill='yellow')
    pole.create_line(0, otrzymanaLinia.get(0), 300, otrzymanaLinia.get(300), width=2, fill='black')
    pole.pack()
    okno.mainloop()

if __name__ == '__main__':
    main()


# todo: siec, animacja?