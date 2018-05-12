class Nuta:
    C = 0
    Cis = 1
    D = 2
    Dis = 3
    E = 4
    F = 5
    Fis = 6
    G = 7
    Gis = 8
    A = 9
    Ais = 10
    B = 11

    def __init__(self, v):
        if(v < self.C or v > self.B):
            raise Exception("Wrong value: " + str(v))

        self.__n = v

    def get(self):
        return self.__n

    def getNoteFromInterval(self, interval):
        val = (self.get() + interval.get()) % 12
        return Nuta(val)

    def __str__(self):
        if(self.__n == self.C):
            return "C"
        elif(self.__n == self.Cis):
            return "Cis"
        elif(self.__n == self.D):
            return "D"
        elif(self.__n == self.Dis):
            return "Dis"
        elif(self.__n == self.E):
            return "E"
        elif(self.__n == self.F):
            return "F"
        elif(self.__n == self.Fis):
            return "Fis"
        elif(self.__n == self.G):
            return "G"
        elif(self.__n == self.Gis):
            return "Gis"
        elif(self.__n == self.A):
            return "A"
        elif(self.__n == self.Ais):
            return "Ais"
        elif(self.__n == self.B):
            return "B"

        return ""

    def __eq__(self, other):
        return self.get() == other.get()

    def getInterval(self, otherNote):
        val =  12+otherNote.get() - self.get()
        return Interwal(val)

class Interwal:
    Pryma = 0
    SekundaMala = 1
    SekundaWielka = 2
    TercjaMala = 3
    TercjaWielka=4
    Kwarta=5
    Tryton = 6
    Kwinta = 7
    SekstaMala=8
    SekstaWielka=9
    SeptymaMala=10
    SeptymaWielka=11
    Oktawa=0

    NonaMala=1
    NonaWielka=2
    DecymaMala=3
    DecymaWielka=4
    Undecyma=5
    UndecymaZwiekszona=6
    #duodecyma
    TerdecymaMala = SekstaMala
    TerdecymaWielka = SekstaWielka

    def __init__(self, val):
        if(val < 0):
            raise Exception('invalid value %d' + str(val))
        self.__val = val%12

    def get(self):
        return self.__val

    def __str__(self):
        if(self.__val == self.Pryma):
            return "Pryma"
        elif(self.__val == self.SekundaMala):
            return "Sekunda Mala"
        elif(self.__val == self.SekundaWielka):
            return "Sekunda Wielka"
        elif(self.__val == self.TercjaMala):
            return "Tercja Mala"
        elif(self.__val == self.TercjaWielka):
            return "Tercja Wielka"
        elif(self.__val == self.Kwarta):
            return "Kwarta"
        elif(self.__val == self.Tryton):
            return "Tryton"
        elif(self.__val == self.Kwinta):
            return "Kwinta"
        elif(self.__val == self.SekstaMala):
            return "Seksta Mala"
        elif(self.__val == self.SekstaWielka):
            return "Seksta Wielka"
        elif(self.__val == self.SeptymaMala):
            return "Septyma Mala"
        elif(self.__val == self.SeptymaWielka):
            return "Septyma Wielka"

        return ""

class Skala:
    # obiekt Nuta() i tablica obiektow Interwal
    def __init__(self, pryma, ciagInterwalow):
        skala = []
        skala.append(pryma)
        for interwal in ciagInterwalow:
            nuta = pryma.getNoteFromInterval(interwal)
            skala.append(nuta)

        # tak lepiej, tuple sa immutable
        self.__skala = tuple(skala)

    def __str__(self):
        outStr = ""
        for i, nuta in enumerate(self.__skala):
            outStr += str(nuta)
            if(i < len(self.__skala)-1):
                outStr+=', '
        return outStr

    def get(self):
        return self.__skala

    @staticmethod
    def getInterwaly():
        return []

class GamaDurowa(Skala):
    def __init__(self, pryma):
        Skala.__init__(self, pryma, GamaDurowa.getInterwaly())

    @staticmethod
    def getInterwaly():
        return [Interwal(Interwal.SekundaWielka),
                Interwal(Interwal.TercjaWielka),
                Interwal(Interwal.Kwarta),
                Interwal(Interwal.Kwinta),
                Interwal(Interwal.SekstaWielka),
                Interwal(Interwal.SeptymaWielka)]


class GamaMolowa(Skala):
    def __init__(self, pryma):
        Skala.__init__(self, pryma, GamaMolowa.getInterwaly())

    @staticmethod
    def getInterwaly():
        return [Interwal(Interwal.SekundaWielka),
                Interwal(Interwal.TercjaMala),
                Interwal(Interwal.Kwarta),
                Interwal(Interwal.Kwinta),
                Interwal(Interwal.SekstaMala),
                Interwal(Interwal.SeptymaMala)]