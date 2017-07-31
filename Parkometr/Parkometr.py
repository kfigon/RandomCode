__author__ = 'kamil'

class Parkometrx():

    __kwantMinut = 15 # minuty minimalnie

    # cena za godzine
    def __init__(self, cena):
        self.__cena = cena
        self.__ileMinut = 0

    def getCenaZaGodzine(self):
        return  self.__cena

    def getIleMinut(self):
        return self.__ileMinut

    def getIleGodzinIMinut(self):
        godziny = int(self.getIleMinut() / 60)
        minuty = self.getIleMinut() - godziny*60

        return godziny,minuty

    def zwiekszMinuty(self):
        self.__ileMinut += self.__kwantMinut

    def zmniejszMinuty(self):
        if(self.getIleMinut() < self.__kwantMinut):
            self.__ileMinut = 0
            return
        self.__ileMinut -= self.__kwantMinut

    def zwiekszGodzine(self):
        self.__ileMinut += 60

    def zmniejszGodzine(self):
        if (self.getIleMinut() < 60):
            self.__ileMinut = 0
            return
        self.__ileMinut -= 60

    # aktualny czas - godizny i minuty
    def liczIle(self, godzina=0, minuty=0):
        return self.getCenaZaGodzine()*self.getIleMinut()/60

