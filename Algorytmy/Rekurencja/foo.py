__author__ = 'kamil'

def silnia(n):
    if(n==0):
        return 1
    return silnia(n-1)*n


def fibonacci(n):
    if(n <= 1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)

# nie rekurencyjnie
def fibonacciX(n):
    if(n<=1):
        return n

    fib_minus1 = 1
    fib_minus2 = 0
    fib = 1
    for i in range(2, n):
        fib_minus2 = fib_minus1
        fib_minus1 = fib
        fib = fib_minus1+fib_minus2

    return fib

def potega(x, y):
    if(y == 0):
        return 1

    return x*potega(x, y-1)

# ciag dany wzorem:
# an = -1 dla n == 1
# an = -a_(n-1) * n - 3 dla n>1
def ciag(n):
    if(n <= 1):
        return -1
    return -1*ciag(n-1)*n-3

# konwersja dziesietna->binarna rekurencyjnie
def konwersjaNaBinarna(liczba):
    napis=""
    napis = konwerInternal(liczba, napis)
    return napis[::-1]

def konwerInternal(liczba, napis):
    if(liczba==0):
        return napis
    napis += str(liczba%2)
    return konwerInternal(int(liczba/2), napis)