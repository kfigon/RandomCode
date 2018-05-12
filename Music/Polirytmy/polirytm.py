class GeneratorPolirytmow:
    def __init__(self, r1, r2):
        self.__r1 = r1
        self.__r2 = r2
    def generuj(self):
        mniejszy = min(self.__r1, self.__r2)
        wiekszy = max(self.__r1, self.__r2)

        out = []
        x=0
        for _ in range(mniejszy):
            inner = []
            for _ in range(wiekszy):
                if x % mniejszy == 0:
                    inner.append('X')
                else:
                    inner.append('O')
                x += 1
            out.append(inner)
        return out

    def __str__(self):
        g = self.generuj()
        out =""
        for wiersz in g:
            for i in wiersz:
                out += i + ' '
            out +='\n'
        return out

if __name__ == '__main__':
    a = int(input('podaj rytm1: '))
    b = int(input('podaj rytm2: '))
    g = GeneratorPolirytmow(a,b)
    print("Jedna reka stuka na 1 kazdego wiersza, druga na X\n")
    print(g)