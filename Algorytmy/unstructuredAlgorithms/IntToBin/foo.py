__author__ = 'kamil'

def foo(liczba):
    if(liczba == 0):
        return '0'

    outStr = ""
    while(liczba >= 1):
        if(liczba % 2 == 0):
            liczba/=2
            outStr += "0"
        else:
            liczba = int(liczba/2)
            outStr += "1"

    return outStr[::-1]
