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

    # tablica!
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
        liczba += 97 # a
    return chr(liczba)

def str2Tab(napis):
    tab = []
    for i in napis:
        tab.append(i)
    return tab


class Populacja:
    def __init__(self, liczebnosc, dlugoscChromosomu, cel, wspolczynnikMutacji=1):
        self.__wspolczynnikMutacji = wspolczynnikMutacji
        self.__cel = cel

        self.__populacja = [None]*liczebnosc
        for i in range(len(self.__populacja)):
            self.__populacja[i] = Chromosom()
            self.__populacja[i].randomize(dlugoscChromosomu)

    def getLiczebnoscPopulacji(self):
        return len(self.__populacja)

    def getFitness(self):
        out = [0]*self.getLiczebnoscPopulacji()
        i=0
        for osobnik in self.__populacja:
            out[i]=osobnik.liczFitness(self.__cel)
            i+=1
        return out

    def __liczSumeFitnessu(self):
        fitnessPopulacji = self.getFitness()
        suma = 0
        for i in fitnessPopulacji:
            suma+=i
        return suma

    def liczSredniFitness(self):
        suma = self.__liczSumeFitnessu()
        return suma/self.getLiczebnoscPopulacji()

    def wybierzXNajlepszych(self, ileWybrac=2):
        sumaFitnessu = self.__liczSumeFitnessu()
        procentowyUdzialFitnessu = self.getFitness()
        for i in range(len(procentowyUdzialFitnessu)):
            procentowyUdzialFitnessu[i] /= sumaFitnessu
            procentowyUdzialFitnessu[i] *= 100

        zwyciezkiProcent = random.randint(0,100)

    def generujNowePokolenie(self):
        pass