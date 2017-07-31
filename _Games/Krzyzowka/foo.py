__author__ = 'kamil'

# to wszystko. Do kontrolera i view i wsio

class Krotka:
    def __init__(self, tekst, haslo, indeksGlownegoHasla):
        self.__tekst = tekst
        self.__haslo= haslo
        self.__indeksHasla = indeksGlownegoHasla
        self.__wpisane=""

    def getTekst(self):
        return self.__tekst
    def getHaslo(self):
        return self.__haslo
    def getIndeks(self):
        return self.__indeksHasla
    def getGlownaLitera(self):
        return self.__haslo[self.getIndeks()]
    def getDlugoscHasla(self):
        return len(self.__haslo)
    def wpiszHaslo(self, haslo):
        self.__wpisane = haslo
    def getWpisaneHaslo(self):
        return self.__wpisane
    def czyPrawidlowe(self):
        return self.getWpisaneHaslo() == self.getHaslo()
    def liczIleLiterIdzieWLewo(self):
        return self.getDlugoscHasla() - (self.getDlugoscHasla() - self.getIndeks())
    def liczIleLiterIdzieWPrawo(self):
        return self.getDlugoscHasla() - self.getIndeks()-1

class Krzyzowka:
    def __init__(self):
        self.__krotka = []

    def getKrotka(self, i):
        return self.__krotka[i]

    def getIleHasel(self):
        return len(self.__krotka)

    def ladujKrotke(self, data):
        self.__krotka.append(data)

    def ruch(self, indeks, haslo):
        krotka = self.getKrotka(indeks)
        krotka.wpiszHaslo(haslo)

    def czyKoniec(self):
        for i in range(self.getIleHasel()):
            kr = self.getKrotka(i)
            if(kr.czyPrawidlowe() == False):
                return False
        return True

    def getNajbardziejWysunietaWLewoKrotka(self):
        najbardziejWysunietaWLewoKrotka = self.getKrotka(0)
        for i in range(self.getIleHasel()):
            kr = self.getKrotka(i)
            if(kr.liczIleLiterIdzieWLewo() > najbardziejWysunietaWLewoKrotka.liczIleLiterIdzieWLewo()):
                najbardziejWysunietaWLewoKrotka = kr
        return najbardziejWysunietaWLewoKrotka

    def getNajbardziejWysunietaWPrawoKrotka(self):
        najbardziejWysunietaWprawooKrotka = self.getKrotka(0)
        for i in range(self.getIleHasel()):
            kr = self.getKrotka(i)
            if(kr.liczIleLiterIdzieWPrawo() > najbardziejWysunietaWprawooKrotka.liczIleLiterIdzieWPrawo()):
                najbardziejWysunietaWprawooKrotka = kr
        return najbardziejWysunietaWprawooKrotka

    def getSzerokoscPlanszy(self):
        lewa = self.getNajbardziejWysunietaWLewoKrotka()
        prawa = self.getNajbardziejWysunietaWPrawoKrotka()

        return lewa.liczIleLiterIdzieWLewo() + prawa.liczIleLiterIdzieWPrawo()+1

    def getOffsetDlaKrotki(self, i):
        kr = self.getKrotka(i)
        return self.getPozycjaGlownegoHasla() - kr.getIndeks()

    def getPozycjaGlownegoHasla(self):
        kr = self.getNajbardziejWysunietaWLewoKrotka()
        return kr.getIndeks()
    def getGlowneHaslo(self):
        wynik=""
        for i in range(self.getIleHasel()):
            kr = self.getKrotka(i)
            wynik += kr.getGlownaLitera()
        return wynik

class KontrolerKrzyzowki:
    def __init__(self):
        self.__krzyzowka = Krzyzowka()

    def zaladujHaslo(self, data):
        self.__krzyzowka.ladujKrotke(data)

    def czyscEkran(self):
        print ("\n" * 100)

    def game(self):
        while(self.__krzyzowka.czyKoniec() == False):
            self.rysujPlansze(True)
            print("index: ")
            i = int(input())
            print("haslo: ")
            haslo = input()
            self.__krzyzowka.ruch(i, haslo)

        self.rysujPlansze(False)
        print("Koniec, wygrana! Glowne haslo: ")
        print(self.__krzyzowka.getGlowneHaslo())
        return True

    def rysujPlansze(self, zPodpowiedziami):
        self.czyscEkran()
        for i in range(self.__krzyzowka.getIleHasel()):
            kr = self.__krzyzowka.getKrotka(i)
            spacje = (" " * self.__krzyzowka.getOffsetDlaKrotki(i))

            print(str(i) + ".\t\t" + spacje + kr.getWpisaneHaslo(), end='')
            print()

        if(zPodpowiedziami):
                print()
                for i in range(self.__krzyzowka.getIleHasel()):
                    kr = self.__krzyzowka.getKrotka(i)

                    print(str(i)+". " + kr.getTekst())
                print()

def zaladujPrzykladami(ktrl):
    ktrl.zaladujHaslo(Krotka("pierwsze 4 litery","abcd", 2))
    ktrl.zaladujHaslo(Krotka("3 litery","abc", 1))
    ktrl.zaladujHaslo(Krotka("3 litery","abc", 0))
    ktrl.zaladujHaslo(Krotka("2 litery","ab", 1))
    ktrl.zaladujHaslo(Krotka("4 litery","abcd", 1))

def graj():
    ktrl = KontrolerKrzyzowki()
    zaladujPrzykladami(ktrl)
    ktrl.game()

