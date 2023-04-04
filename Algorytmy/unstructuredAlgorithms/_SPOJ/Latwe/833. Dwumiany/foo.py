__author__ = 'kamil'

def foo(n, k):
    licznik = silnia(n)
    mianownik = silnia(k)*silnia(n-k)
    return licznik/mianownik

def silnia(k):
    if(k <= 1):
        return 1
    return silnia(k-1)*k
