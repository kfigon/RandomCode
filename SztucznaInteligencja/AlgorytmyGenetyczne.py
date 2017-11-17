__author__ = 'kamil'
import random

# klasa bazowa tak by wygladala
# class ChromosomBase:
#mutuj, krzyzuj, liczFItness

class Chromosom:
    def __init__(self, inputData=[]):
        self.__tab = inputData

    def randomize(self, dlugoscChromosomu):
        self.__tab.clear()
        self.__tab = ['a']*dlugoscChromosomu
        for i in range(self.getDlugosc()):
            self.__tab[i]=losujLitere()

    def getDlugosc(self):
        return len(self.__tab)

    def mutuj(self, progProcentowy):
        wylosowanyProcent = random.randint(1,100)
        if(wylosowanyProcent <= progProcentowy):
            wylosowanyIndeks = random.randint(0, self.getDlugosc()-1)
            self.__tab[wylosowanyIndeks] = losujLitere()

    def krzyzuj(self, chromosom, startIndex):
        tab1 = self.getAsTab()
        tab2 = chromosom.getAsTab()
        for i in range(startIndex, len(tab1)):
            tab1[i] = tab2[i]

        return Chromosom(tab1)

    # input - tablica
    def liczFitness(self, ideal):
        procentBledow = 0
        for i in range(len(ideal)):
            if(self.__tab[i] != ideal[i]):
                procentBledow+=1
        return (len(ideal)-procentBledow)/len(ideal)*100

    def __str__(self):
        out = ""
        for i in self.__tab:
            out += i
        return out

    def getAsTab(self):
        napis = str(self)
        return str2Tab(napis)

# <0;25> + 1 spacja
def losujLitere():
    liczba = random.randint(0,25)
    if(liczba == 0):
        liczba = 32 # spacja
    else:
        liczba += 96 # a
    return chr(liczba)

def str2Tab(napis):
    tab = []
    for i in napis:
        tab.append(i)
    return tab


class Populacja:
    def __init__(self, liczebnosc, cel, wspolczynnikMutacji=1):
        self.__wspolczynnikMutacji = wspolczynnikMutacji
        self.__cel = cel
        dlugoscChromosomu = len(cel)

        self.__populacja = [None]*liczebnosc
        for i in range(len(self.__populacja)):
            self.__populacja[i] = Chromosom()
            self.__populacja[i].randomize(dlugoscChromosomu)

    def getDlugoscChromosomU(self):
        return len(self.__cel)

    def getLiczebnoscPopulacji(self):
        return len(self.__populacja)

    def liczFitnessKazdegoOsobnika(self):
        out = [0]*self.getLiczebnoscPopulacji()
        i=0
        for osobnik in self.__populacja:
            out[i]=osobnik.liczFitness(self.__cel)
            i+=1
        return out

    def __liczSumeFitnessu(self):
        fitnessPopulacji = self.liczFitnessKazdegoOsobnika()
        suma = 0
        for i in fitnessPopulacji:
            suma+=i
        return suma

    def liczSredniFitness(self):
        suma = self.__liczSumeFitnessu()
        return suma/self.getLiczebnoscPopulacji()

    def wybierzXNajlepszych(self, ileWybrac=2):
        fitnesy = self.liczFitnessKazdegoOsobnika()
        r = Ruletka(fitnesy)

        zwyciezcy =[]
        for i in range(ileWybrac):
            zwyciezkiProcent = random.randint(1,100)
            zwyciezcy.append(r.wybierzIndeksZwyciezcy(zwyciezkiProcent))
        return zwyciezcy

    def generujNowePokolenie(self):
        nowaPopulacja = [None]*self.getLiczebnoscPopulacji()
        for i in range(len(nowaPopulacja)):
            zwyciezcy = self.wybierzXNajlepszych(2)
            rodzicA = self.__populacja[zwyciezcy[0]]
            rodzicB =self.__populacja[zwyciezcy[1]]
            idx = random.randint(1, self.getDlugoscChromosomU())
            dziecko = rodzicA.krzyzuj(rodzicB, idx)
            dziecko.mutuj(self.__wspolczynnikMutacji)
            nowaPopulacja[i]=dziecko

        self.__populacja.clear()
        self.__populacja=nowaPopulacja

    def piszPopulacje(self):
        for i in self.__populacja:
            print(str(i))

    def getNajlepszy(self):
        najlepszyIdx=0
        for i in range(self.getLiczebnoscPopulacji()):
            aktualnyOsobnik = self.__populacja[i]
            najlepszyOsobnik = self.__populacja[najlepszyIdx]

            if(najlepszyOsobnik.liczFitness(self.__cel) < aktualnyOsobnik.liczFitness(self.__cel)):
                najlepszyIdx = i

        return self.__populacja[najlepszyIdx]

class Ruletka:
    def __init__(self, tab):
        self.__tab = tab
        self.__suma = 0
        for i in self.__tab:
            self.__suma+=i

    def getSuma(self):
        return self.__suma

    # wartosci od <1:100>
    def wybierzIndeksZwyciezcy(self, val):
        if(val < 1 or val > 100):
            raise Exception("niewlasciwy parametr ruletki " + str(val))

        suma = self.getSuma()
        # przejscie z procentu na wartosc
        wlasciwaWartosc = (val*suma)/100

        v = self.__tab[0]
        indexToReturn = 0
        for i in range(1, len(self.__tab)):
            if(wlasciwaWartosc <= v ):
                return indexToReturn
            indexToReturn+=1
            v += self.__tab[i]

        return indexToReturn


if __name__=='__main__':
    cel = "byc albo nie byc"
    p = Populacja(500, str2Tab(cel), 5)

    sredniFitness = p.liczSredniFitness()
    fitness = sredniFitness
    nrPopulacji=0
    print("start")
    najlepszy = p.getNajlepszy()
    while(fitness < 100):
        nrPopulacji+=1
        p.piszPopulacje()

        print("---->populacja nr %d, sredni fitness %d, najlepszy %d: %s" % (nrPopulacji, sredniFitness, fitness, str(najlepszy)))
        sredniFitness = p.liczSredniFitness()
        p.generujNowePokolenie()
        najlepszy = p.getNajlepszy()
        fitness = najlepszy.liczFitness(str2Tab(cel))

    print("skonczylem, ile populacji: %d" % nrPopulacji)
    print("najlepszy: %s" % (str(najlepszy)))