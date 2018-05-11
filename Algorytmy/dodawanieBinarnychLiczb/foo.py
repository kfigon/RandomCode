__author__ = 'kamil'

# zawsze zwracaj N+1 dluga tablice

# dodawanie 2 binarnych liczb zapisanych w tablicach
def dodaj(a, b):

    out = [0]*(len(a)+1)

    przeniesienie = 0
    # tak jak pisemnie - od prawej do lewej
    for i in reversed(range(len(a))):
        suma = a[i]+b[i] + przeniesienie
        if(suma == 0 or suma == 1):
            out[i+1]=suma       # i+1 bo out jest dluzszy o 1 bit
            przeniesienie = 0
        elif(suma == 2):
            przeniesienie = 1
            out[i+1]=0
        else:
            przeniesienie=1
            out[i+1]=1

    # skrajnie lewy bit
    if(przeniesienie == 1):
        out[0]=1

    return out
