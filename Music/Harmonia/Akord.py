from Music.Harmonia.Nuta import *

class TrybAkordu:
    Dur=0
    Mol=1
    Sus4=2
    Sus2=3
    PowerChord=4

class RodzajAkordu:
    BrakSeptymy=0
    SeptymaWielka=1
    Dominantowy=2

class Akord:
    def __init__(self, listaNut):
        self.__nuty = tuple(listaNut)

    def get(self):
        return self.__nuty

    def __str__(self):
        outStr = ""
        outStr += str(self.__nuty[0])
        tryb = self.getTryb()
        if(tryb == TrybAkordu.Dur):
            outStr += "dur"
        return outStr

    def getTryb(self):
        pryma = self.__nuty[0]
        tercjaWielka = pryma.getNoteFromInterval(Interwal(Interwal.TercjaWielka))
        tercja = self.__nuty[1]
        roznicaPoltonow = tercja.get() - tercjaWielka.get()
        if(roznicaPoltonow == 0):
            return TrybAkordu.Dur
        elif(roznicaPoltonow == -1):
            return TrybAkordu.Mol
        elif(roznicaPoltonow == -2):
            return TrybAkordu.Sus2
        elif(roznicaPoltonow == 1):
            return TrybAkordu.Sus4
        else:
            return TrybAkordu.PowerChord

    def getRodzaj(self):
        pryma = self.__nuty[0]
        return RodzajAkordu.BrakSeptymy

class AkordBuilder:
    def __init__(self, listaNut):
        self.__nuty = listaNut

    def build(self):
        pass