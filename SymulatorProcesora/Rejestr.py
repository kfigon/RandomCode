__author__ = 'kamil'

class Rejestr:
    def __init__(self, val=0):
        self.__val = 0
        self.set(val)

    def get(self):
        return self.__val

    def set(self, val):
        self.__val = (val & 0xffff)
    def setUpper(self, val):
        self.__val = (val & 0xff)<<8
    def setLower(self, val):
        self.__val = (val & 0xff)
    def getUpper(self):
        return ((self.__val>>8) & (0xff))

    def getLower(self):
        return (self.__val & 0xff)

    def __str__(self):
        return hex(self.__val)