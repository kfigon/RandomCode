__author__ = 'kamil'
from SymulatorProcesora.Rejestr import Rejestr

class Procesor:
    def __init__(self):
        self.__ax = Rejestr()
        self.__bx = Rejestr()
        self.__cx = Rejestr()
        self.__dx = Rejestr()

    def parseCommand(self, command):
        command.capitalize()
        cmd = command.split(' ')
        if(len(cmd) <= 1 or (len(cmd) == 2 and cmd[0] != 'GET')):
            raise Exception("niewlasciwa komenda " + command)

        if(cmd[0] == 'GET'):
            return self.__getRegVal(cmd[1])
        elif(cmd[0] == 'MOV'):
            self.__mov(cmd[1], int(cmd[2], 16))
            return 0
        elif(cmd[0] == 'ADD'):
            self.__add(cmd[1], cmd[2])
            return 0
        elif(cmd[0] == 'SUB'):
            self.__sub(cmd[1], cmd[2])
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
