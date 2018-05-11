import matplotlib.pyplot as plt
import math
import random

def probkujBity(bity, czasTrwaniaTransmisji, fp):
    out = []
    ileProbekNaBit = int((czasTrwaniaTransmisji*fp)/len(bity))
    for b in bity:
        for _ in range(ileProbekNaBit):
            out.append(b)
    return out

def main():
    czasTrwaniaBitu = 0.5 # [s]
    fprobkowania = 30
    fnosnej = 2

    czasTrwaniaTransmisji = 20 # [s]

    ileBitow = round(czasTrwaniaBitu*czasTrwaniaTransmisji)
    bity = [random.randint(0,1) for i in range(ileBitow)]
    probkiBitow = probkujBity(bity, czasTrwaniaTransmisji, fprobkowania)

    czas = [i/fprobkowania for i in range(0, czasTrwaniaTransmisji*fprobkowania)]
    nosna = [math.cos(2*math.pi*fnosnej*czas[i]) for i in range(len(czas))]

    zmodulowany = []
    for i in range(len(nosna)):
        ampl = 1
        if(probkiBitow[i] == 0):
            ampl = 0.3
        zmodulowany.append(ampl*nosna[i])

    plt.subplot(3,1,1)
    plt.stem(probkiBitow)

    plt.subplot(3,1,2)
    plt.stem(nosna)

    plt.subplot(3,1,3)
    plt.stem(zmodulowany)

    plt.show()

if __name__ == '__main__':
    main()