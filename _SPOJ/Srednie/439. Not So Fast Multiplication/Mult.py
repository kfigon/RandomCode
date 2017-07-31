def mult(a ,b):
    if(a == "0" or b == "0"):
        return "0"

    first = a[::-1]
    second = b[::-1]
    wynikiCzastkowe = []

    for s in second:
        pojedynczyWynikCzatkowy=""
        carry=0
        for f in first:
            temp = int(s)*int(f) + carry
            # zalatw przeniesienia
            if(temp >= 10):
                ileDziesiatek = wyciagnijDziesiatki(temp)
                temp -= ileDziesiatek * 10
                carry = ileDziesiatek
            else:
                carry=0
            pojedynczyWynikCzatkowy+=str(temp)
        # przeniesienie na koncu
        if(carry > 0):
            pojedynczyWynikCzatkowy+=str(carry*10)

        wynikiCzastkowe.append(pojedynczyWynikCzatkowy[::-1])

    return sumuj(wynikiCzastkowe)

def wyciagnijDziesiatki(a):
    a/=10
    return int(a)

def sumuj(wynikiCzastkowe):
    result = 0
    dziesiatki=1
    for wynikCzastkowy in wynikiCzastkowe:
        result += int(wynikCzastkowy) * dziesiatki
        dziesiatki*=10

    return str(result)