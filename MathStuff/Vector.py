from math import sqrt
from math import atan2
from math import sin
from math import cos

# immutable!
class Vector:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    @staticmethod
    def stworzZModuluIKata(modul, kat):
        x = modul*cos(kat)
        y=modul*sin(kat)
        return Vector(x,y)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def __str__(self):
        return "(%d,%d)" % (self.__x, self.__y)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.__x == other.getX() and self.__y == other.getY())

    def __add__(self, other):
        return Vector(self.__x + other.getX(), self.__y + other.getY())

    def __sub__(self, other):
        return Vector(self.__x - other.getX(), self.__y - other.getY())

    def dodajSkalar(self, val):
        return Vector(self.__x+val, self.__y+val)

    def odejmijSkalar(self, val):
        return Vector(self.__x-val, self.__y-val)

    def mnoz(self,skalar):
        return Vector(self.__x*skalar, self.__y*skalar)

    def dziel(self,skalar):
        return Vector(self.__x/skalar, self.__y/skalar)

    def getDlugosc(self):
        return sqrt(self.__x**2 + self.__y**2)

    # w radianach
    def getKat(self):
        return atan2(self.__y,self.__x)

    def obroc(self, katRadiany):
        kat = self.getKat()+katRadiany
        return Vector.stworzZModuluIKata(self.getDlugosc(), kat)

    def getPostacTrygonometryczna(self):
        return (self.getDlugosc(), self.getKat())

    def normalizuj(self):
        modul = self.getDlugosc()
        return Vector(self.__x/modul, self.__y/modul)