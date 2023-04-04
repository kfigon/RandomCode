__author__ = 'kamil'

def foo(x):
    output = konwertuj(x, 16) + " " + konwertuj(x, 11)
    return output

def konwertuj(x, base):
    out = ""
    while(x >= 1):
        out += zamienLiczbeNaLitere(x%base, base)
        x = int(x/base)

    return out[::-1]

def zamienLiczbeNaLitere(liczba, baza):
    if liczba == 10:
        return "A"
    if(baza == 16):
        if (liczba == 11): return "B"
        elif (liczba == 12): return "C"
        elif (liczba == 13): return "D"
        elif (liczba == 14): return "E"
        elif (liczba == 15): return "F"
        else: return str(liczba)
    else:
        return str(liczba)