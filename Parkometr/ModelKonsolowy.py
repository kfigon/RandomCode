__author__ = 'kamil'

from Parkometr import Parkometrx

class ModelKonsolowyParkometru():
    def __init__(self):
        self.__parkometr = Parkometrx(3)

    def zwiekszMinuty(self):
        self.__parkometr.zwiekszMinuty()

    def zmniejszMinuty(self):
        self.__parkometr.zmniejszMinuty()

    def zwiekszGodzine(self):
        self.__parkometr.zwiekszGodzine()

    def zmniejszGodzine(self):
        self.__parkometr.zmniejszGodzine()

    def piszWybranyCzas(self):
        godziny,minuty = self.__parkometr.getIleGodzinIMinut()
        print("Wybrano %d:%d" % (godziny, minuty))

    def piszCeneZaGodizne(self):
        print("Cena za godzine %d" % self.__parkometr.getCenaZaGodzine())

    def piszKwote(self):
        print("Do zaplacenia %.2f zl" % self.__parkometr.liczIle())