import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack

f = 1

step = 0.1 # sampling step
t = np.arange(0,30,step)
y = np.cos(2*3.1415*f *t)


plt.subplot(3,2,1)
plt.title('Sygnal <0;30) krok 0.1')
plt.xlabel('time')
plt.ylabel('cos(2pi*n)')
plt.plot(t,y)

# liczy DFT (dla skonczonych). 
# DTFT jest dla okresowych
yt = scipy.fftpack.fft(y)

plt.subplot(3,2,3)
plt.title('Fourier Re')
plt.stem(t, np.real(yt))

plt.subplot(3,2,4)
plt.title('Fourier Imag')
plt.stem(t, np.imag(yt))

plt.subplot(3,2,5)
plt.title('Fourier abs')
plt.stem(t, np.abs(yt))

plt.subplot(3,2,6)
plt.title('Fourier phas')
plt.stem(t, np.angle(yt))


plt.show()

Fs = 1/step
resolution = Fs/(300) # Fs/N, N dlugosc sygnalu
numerProbkiZPikiem = 30
czestotliwoscSygnalu = numerProbkiZPikiem * resolution
print('czestotliwosc: ' + str(czestotliwoscSygnalu))

'''
pik cosinusa na probce '3', czyli 30 (indeks od 0, krok 0.1)
dlugosc sygnalu to 300. czestotliwosc to 1. jakas faza sie pojawila, bo imag niezerowy (nie powinno tutaj byc nic?)

w = numerProbkiZPikiem * 2pi/dlugoscSygnalu
czestotliwosc: skoro max f to fs/2 i odpowiada ono N/2, dzielac jedno przez drugie dostajemy Fs/N <- rozdzielczosc wykresu
label - skoro max cz. to Fs/2 i wychodzi w polowie fouriera (N/2), mozna wyskalowac wykres
'''