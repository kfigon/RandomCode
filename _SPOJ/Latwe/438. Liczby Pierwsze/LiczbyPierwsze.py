# brute force
def fun(liczba):
    if(liczba == 0 or liczba == 1):
        return "NIE"

    for i in range(2, liczba):
        if(liczba % i == 0):
            return "NIE"

    return "TAK"

# sito
def fun2(liczba):

    if(liczba < 2):
        return "NIE"

    isPrime = [True] * (liczba+1)

    import math
    granica = (int)(math.sqrt(liczba))

    for i in range(2, granica+1):
        # wykreslamy wielokrotnosci:
        for j in range(i+i, liczba+1, i):
            isPrime[j]=False

    if(isPrime[liczba]):
        return "TAK"
    else:
        return "NIE"