# Sign bit: 1 bit
# Exponent width: 8 bits
# Significand precision: 24 bits
# (23 explicitly stored)

def foo(liczba):

    # zakladam te bajty jako big endian
    # najstarszy bajt to [0]
    # bajty = [0] * 4

    bitZnaku = 0
    if(liczba < 0):
        bitZnaku = 1

    #wynik = -1^bitZnaku * (1,bityMantysy) * 2^(wykladnik-127)

    mantysa = 0
    czescUlamkowa = liczba - int(liczba)

    import math
    iloraz = czescUlamkowa
    potega = 0

    while(iloraz < 1):
        potega -=1
        iloraz = czescUlamkowa / math.pow(2, potega)

    wykladnik = 127 + potega

    mantysa = iloraz - 1
    mantysaStrBin = "0b"

    for bit in range(23):
        mantysa *= 2
        if(mantysa == 1):
            mantysaStrBin += '1'
            break
        elif(mantysa > 1):
            mantysaStrBin += '1'
            mantysa -= 1
        else:
            mantysaStrBin += '0'

    print("liczba: ", liczba)
    print(bitZnaku, " ", hex(wykladnik)," ", hex(int(mantysaStrBin,2)))
    print(bitZnaku, " ", bin(wykladnik)," ", mantysaStrBin)

    return ""

foo(0.085)
# actual:  0b 0111101101011100001010001111010
# expected 0b00111101101011100001010001111011
# czyli prawie, tylko parsowanie