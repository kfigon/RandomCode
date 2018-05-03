import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack

f = 1
t = np.arange(0,10,0.1)
y = np.cos(2*3.1415*f *t)


plt.subplot(4,1,1)
plt.title('Sygnal <0;10) krok 0.1')
plt.xlabel('time')
plt.ylabel('cos(2pi*n)')
plt.plot(t,y)

# liczy DFT (dla skonczonych). 
# DTFT jest dla okresowych
yt = scipy.fftpack.fft(y)

plt.subplot(4,1,2)
plt.title('Fourier Re')
plt.stem(t, np.real(yt))

plt.subplot(4,1,3)
plt.title('Fourier Imag')
plt.stem(t, np.imag(yt))

plt.subplot(4,1,4)
plt.title('Fourier abs')
plt.stem(t, np.abs(yt))

plt.show()

'''
pik cosinusa na probce '1', czyli 10 (indeks od 0, krok 0.1)
dlugosc sygnalu to 100. czestotliwosc to 1. jakas faza sie pojawila, bo imag niezerowy

label - skoro max cz. to Fs/2 i wychodzi w polowie fouriera (N/2), mozna wyskalowac wykres
'''