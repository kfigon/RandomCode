def foo(napis):
    napisOut=""

    i=0
    while i < len(napis):
        aktualnaLitera = napis[i]
        ileRazy = ileTakichSamychLiterDoPrzodu(napis, i)
        if(ileRazy >=3):
            napisOut+=aktualnaLitera+str(ileRazy)
            i+=ileRazy   # w for to nie zadziala :(
            continue
        else:
            napisOut+=aktualnaLitera
        i+=1

    return napisOut

def ileTakichSamychLiterDoPrzodu(napis, startIdx):
    poszukiwanaLitera = napis[startIdx]
    licznik = 0

    for i in range(startIdx, len(napis)):
        if(napis[i] == poszukiwanaLitera):
            licznik+=1
        else:
            break

    return licznik