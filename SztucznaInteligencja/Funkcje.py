import math as m

class Funkcja:
    def get(self, x):
        return 0
    def __str__(self):
        return ""

class FunkcjaLiniowa(Funkcja):
    def __init__(self,a, b):
        self.__a=a
        self.__b=b
    def get(self, x):
        return self.__a*x + self.__b
    def __str__(self):
        return ("f(x) = %dx + %d" %(self.__a, self.__b))

class Sigmoida(Funkcja):
    def get(self, x):
        if(x<=-10):
            return 0
        elif(x>=10):
            return 1
        return 1/(1+m.e**(-x))
    def __str__(self):
        return ("f(x) = 1/(1+exp(-x)")

class Signum(Funkcja):
    def get(self, x):
        if(x < 0):
            return -1
        return 1
    def __str__(self):
        return ("f(x) = signum(x)")