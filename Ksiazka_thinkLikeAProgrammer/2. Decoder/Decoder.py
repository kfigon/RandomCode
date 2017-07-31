class State:
    U=1
    L=2
    P=3

    def __init__(self):
        self.__state = State.U

    def nextState(self):
        self.__state = self.__state % 3 + 1

    def getModuloCounter(self):
        if(self.__state == State.L or
           self.__state == State.U):
            return 27
        else:
            return 9
    def getState(self):
        return self.__state

class DecoderX:
    def __init__(self):
        self.__state = State()

    def feed(self, liczba):
        result = liczba % self.__state.getModuloCounter()
        if(result == 0):
            self.__state.nextState()
            return ""
        else:
            return self.getZnak(result)

    def getZnak(self, result):
        if(self.__state.getState() == State.U):
            result += 64
            return chr(result).upper()
        elif(self.__state.getState() == State.L):
            result += 64
            return chr(result).lower()
        else:
            return self.getPunctuation(result)

    def getPunctuation(self, znak):
        return {
            1: '!',
            2: '?',
            3: ',',
            4: '.',
            5: ' ',
            6: ';',
            7: '\"',
            8: '\'',
        }[znak]
