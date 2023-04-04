def foo(tab):
    liczby = preprocess(tab)

    outTab = []
    for i in reversed(liczby):
        if(czyIstnieje(outTab, i) == False):
            outTab.append(i)

    return postprocess(outTab)

def preprocess(strTab):
    liczby = []
    for i in strTab:
        if(i != ' '):
            liczby.append(int(i))

    return liczby

def czyIstnieje(intTab, liczba):
    for i in intTab:
        if(i == liczba):
            return True

    return False

def postprocess(liczby):
    strTab = ""
    for i in liczby:
        strTab+=str(i) + " "

    # usun ostatni znak
    strTab = strTab[:-1]

    # "algorytmicznie", bez pythona normalnego fora
    # i nie dodawac spacji na ostatnim

    return strTab