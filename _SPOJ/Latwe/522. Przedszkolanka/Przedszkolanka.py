# najmniejsza wspolna wielokrotnosc
def foo(a,b):
    return int((a*b)/nwd(a,b))

def nwd(a,b):
    while(a != 0 and b!=0):
        min = minimum(a,b)
        maks = maksimum(a,b)

        a=min
        b=maks % min

    return maksimum(a,b)

def minimum(a,b):
    if(a<b):
        return a
    return b

def maksimum(a,b):
    if(a>b):
        return a
    return b