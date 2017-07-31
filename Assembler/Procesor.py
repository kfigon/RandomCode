__author__ = 'kamil'

class Util:
    def ileBajtow(liczba):
        ileBajtow = 0
        while (liczba != 0):
            liczba >>= 8
            ileBajtow += 1

        return ileBajtow

class Reg:
    #ogolnego przeznaczenia
    class GP:
        R0 = 0
        R1 = 1
        R2 = 2
        R3 = 3
        R4 = 4
        R5 = 5
        R6 = 6
        R7 = 7
        R8 = 8
        R9 = 9
        R10 = 10
        R11 = 11
        R12 = 12
        R13 = 13
    class Flow:
        PC = 14    # program counter
        SP = 15    # stack pointer
    # class Spec:
    #     FR =  # flag register
    # class Control:
    #     Int0 = 0x100
    #     Int1 = 0x101
    #     Int2 = 0x103
    #     Int3 = 0x104
    #     Int4 = 0x105
    #     Int5 = 0x106
    #     Int6 = 0x107

class BajtAraj:
    def __init__(self, size):
        self.__array = [0 for i in range(size)]

    def __validateReg(self, val):
        if(val > len(self.__array) or val < 0):
            raise IndexError

    def get(self, reg):
        self.__validateReg(reg)
        return self.__array[reg]

    def set(self, reg, val):
        self.__validateReg(reg)
        self.__array[reg] = val

class Rejestry(BajtAraj):
    def __init__(self):
        super().__init__(16)

class Pamiec(BajtAraj):
    def __init__(self):
        super().__init__(1024)

    def set(self, reg, val):
        ileBajtow = Util.ileBajtow(val)

        for i in range(ileBajtow):
            valueToWrite = (val >> (i*8)) & 0xff
            super().set(reg + i, valueToWrite)

class Procesor:
    def __init__(self):
        self.__rejestry = Rejestry()
        self.__pamiec = Pamiec()

    def getRejestr(self, rejestr):
        return self.__rejestry.get(rejestr)

    def czytajAdres(self, adres):
        return self.__pamiec.get(adres)

    def zapiszPodAdres(self, adres, bajt):
        self.__pamiec.set(adres, bajt)

    def set(self, reg, val):
        self.__rejestry.set(reg, val)

    def mov(self, dst, src):
        srcVal = self.getRejestr(src)
        self.set(dst, srcVal)

    def ld(self, dst, src):
        adres = self.getRejestr(src)
        memVal = self.czytajAdres(adres)
        self.set(dst, memVal)

    def st(self, dst, src):
        adres = self.getRejestr(dst)
        wartosc = self.getRejestr(src)
        self.zapiszPodAdres(adres, wartosc)

    def add(self, dst, src):
        a = self.getRejestr(dst)
        b = self.getRejestr(src)
        self.set(dst, a+b)

    def sub(self, dst, src):
        a = self.getRejestr(dst)
        b = self.getRejestr(src)
        self.set(dst, a-b)

    def mul(self, dst, src):
        a = self.getRejestr(dst)
        b = self.getRejestr(src)
        self.set(dst, a*b)