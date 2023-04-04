def foo(liczba):

    licznik=0
    while not czyPalidrom(liczba):
        liczba = liczba + odwroc(liczba)
        licznik +=1
    return (str(liczba) + " " + str(licznik))

def czyPalidrom(liczba):
    if(liczba == odwroc(liczba)):
        return True
    else:
        return False

def odwroc(liczba):
    liczbaStr=str(liczba)
    liczbaStr = liczbaStr[::-1]
    return int(liczbaStr)