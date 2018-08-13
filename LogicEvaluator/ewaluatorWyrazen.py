import unittest

class GeneratorLogiki:    
    def __parseCharToBool(self,binary):
        for b in binary:
            yield True if b=='1' else False

    def generuj(self, ileZmiennych):
        out=[None]*(2**ileZmiennych)
        szablon = '0%db' % ileZmiennych
        for i in range(len(out)):
            liczba = format(i, szablon)
            out[i] = list(self.__parseCharToBool(liczba))
        return out

class EwaluatorWyrazen:
    def foo(self,wyrazenie, ileZmiennych):
        g = GeneratorLogiki()
        mozliwosciLogiczne = g.generuj(ileZmiennych)
        wyniki = []
        for i in mozliwosciLogiczne:
            w = wyrazenie(*i)
            wyniki.append(w)
        return wyniki

    def porownajWyniki(self,przed, po):
        if(len(przed) != len(po)):
            return False
        
        for i in range(len(przed)):
            if(przed[i] != po[i]):
                return False
        return True

    def piszArgumentyIWyniki(self, args, wynikA, wynikB):
        print("%r != %r dla:" % (wynikA, wynikB))
        print(args)
        print()
        
    def sprawdzWyrazenia(self, wyrA, wyrB, ileZmiennych):
        wynikiA = self.foo(wyrA, ileZmiennych)
        wynikiB = self.foo(wyrB, ileZmiennych)
        if(self.porownajWyniki(wynikiA, wynikiB)):
           print("to samo!")
        else:
            print("blad! Oto lista:\n")
            print(wynikiA)
            print(wynikiB)

            print("\nszczegolowe argumenty:")
            g = GeneratorLogiki()
            mozliwosciLogiczne = g.generuj(ileZmiennych)
            for i in range(len(wynikiA)):
                wA = wynikiA[i]
                wB = wynikiB[i]
                arg = mozliwosciLogiczne[i]
                if(wA != wB):
                    self.piszArgumentyIWyniki(arg, wA, wB)


if __name__ == '__main__':
    ew = EwaluatorWyrazen()
    ew.sprawdzWyrazenia(lambda w,x,y,z: not(x or y or w or z),
                        lambda w,x,y,z: not x and not y and not z and not w,
                        4)
