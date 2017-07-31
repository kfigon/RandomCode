def liczSilnie(liczba):
    if(liczba==1):
        return 1
    else:
        return liczba*liczSilnie(liczba-1)

def foo(liczba):
    asd = liczSilnie(liczba)

    jednosci = asd % 10
    dziesiatki = int((asd % 100)/10)

    return (str(dziesiatki) + " " + str(jednosci))
