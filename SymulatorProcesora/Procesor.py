__author__ = 'kamil'
from SymulatorProcesora.Rejestr import Rejestr

class Komenda:
    def __init__(self, komenda, arg1, arg2=None):
        self.__komenda = komenda
        self.__arg1=arg1
        self.__arg2=arg2

    def getKomenda(self):
        return self.__komenda

    def getArgs(self):
        return self.__arg1,self.__arg2

    @staticmethod
    def parse(string):
        string.capitalize()
        cmd = string.split(' ')
        if(len(cmd) <= 1 or (len(cmd) == 2 and cmd[0] != 'GET')):
            raise Exception("niewlasciwa komenda " + string)

        if(len(cmd) == 3):
            return Komenda(cmd[0], cmd[1], cmd[2])
        elif(len(cmd) == 2):
            return Komenda(cmd[0], cmd[1], None)

class Procesor:
    def __init__(self):
        self.__ax = Rejestr()
        self.__bx = Rejestr()
        self.__cx = Rejestr()
        self.__dx = Rejestr()

    def parseAndExecute(self, command):
        komenda = Komenda.parse(command)
        return self.executeCommand(komenda)

    def executeCommand(self, komenda):
        if(komenda.getKomenda() == 'GET'):
            a1,a2 = komenda.getArgs()
            return self.__getRegVal(a1)
        elif(komenda.getKomenda() == 'MOV'):
            a1,a2 = komenda.getArgs()
            self.__mov(a1, int(a2, 16))
            return 0
        elif(komenda.getKomenda() == 'ADD'):
            a1,a2 = komenda.getArgs()
            self.__add(a1,a2)
            return 0
        elif(komenda.getKomenda() == 'SUB'):
            a1,a2 = komenda.getArgs()
            self.__sub(a1,a2)
            return 0
        else:
            raise Exception("invalid command")

    def __mov(self, reg, val):
        if(reg == "AH"):
            self.__ax.setUpper(val)
        elif(reg=="AL"):
            self.__ax.setLower(val)
        elif(reg=="BH"):
            self.__bx.setUpper(val)
        elif(reg=="BL"):
            self.__bx.setLower(val)
        elif(reg=="CH"):
            self.__cx.setUpper(val)
        elif(reg=="CL"):
            self.__cx.setLower(val)
        elif(reg=="DH"):
            self.__dx.setLower(val)
        elif(reg=="DL"):
            self.__dx.setLower(val)
        else:
            raise Exception("nie ma takiego rejestru!")

    def __getRegVal(self, reg):
        if(reg == "AH"):
            return self.__ax.getUpper()
        elif(reg=="AL"):
            return self.__ax.getLower()
        elif(reg=="BH"):
            return self.__bx.getUpper()
        elif(reg=="BL"):
            return self.__bx.getLower()
        elif(reg=="CH"):
            return self.__cx.getUpper()
        elif(reg=="CL"):
            return self.__cx.getLower()
        elif(reg=="DH"):
            return self.__dx.getUpper()
        elif(reg=="DL"):
            return self.__dx.getLower()
        else:
            raise Exception ("nie ma takiego rejestru!")

    def __add(self, reg1, reg2):
         val1 = self.__getRegVal(reg1)
         val2 = self.__getRegVal(reg2)
         self.__mov(reg1, val1+val2)

    def __sub(self, reg1, reg2):
        val1 = self.__getRegVal(reg1)
        val2 = self.__getRegVal(reg2)
        self.__mov(reg1, val1-val2)

    def __str__(self):
        out = "AX: %s\n" \
              "BX: %s\n" \
              "CX: %s\n" \
              "DX: %s" % \
              (str(self.__ax),
               str(self.__bx),
               str(self.__cx),
               str(self.__dx))
        return out
