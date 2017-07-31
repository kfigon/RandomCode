def doubleDigit(liczba):
    liczba *= 2
    if (liczba >= 10):
        return 1 + (liczba % 10)
    else:
        return liczba


# idealnie - pobierac znak po znaku
# wtedy trzeba sledzic sume dla przypadku
# gdy znak ktory trzeba doubleDigit()
# wypada w zaleznosci od dotychczasowej
# liczby znakow - oddCheckSum i evenChekSUm
# liczyc oddzielnie, a gdy poprosza o wynik
# wypluc jeden z dwocj
def foo(number):
    checkSum = 0
    strNumber = str(number)

    i = 0
    for znak in reversed(strNumber):
        if (i % 2 == 0):
            checkSum += doubleDigit(int(znak))
        else:
            checkSum += int(znak)
        i += 1

    print(strNumber + " -> " + str(checkSum))
    return checkSum % 10 == 0