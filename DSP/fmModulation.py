import matplotlib.pylab as plt
import numpy as np

def stemplot():
    data = [1,0,0,0,1,1,1,0,1,1, 3]

    _, _, baseline = plt.stem(data)
    plt.setp(baseline, color='r', linewidth=2)
    plt.show()

def cosplot():
    x = np.linspace(0.1, 2 * np.pi)
    markerline, stemlines, baseline = plt.stem(x, np.cos(x))
    plt.setp(baseline, color='r', linewidth=2)
    plt.show()

def fmMod():
    fmod = 4.0
    fcarrier = 40.0

    time = np.arange(1000) / 1000
    modulator = np.sin(2.0 * np.pi * fmod * time)
    carrier = np.sin(2.0 * np.pi * fcarrier * time)
    result = np.zeros_like(modulator)

    for i, t in enumerate(time):
        result[i] = np.sin(2.0 * np.pi * (fcarrier * t + modulator[i]))


    plt.subplot(3, 1, 1)
    plt.title('Frequency Modulation')
    plt.plot(modulator)
    plt.ylabel('Amplitude')
    plt.xlabel('Modulator signal')

    plt.subplot(3, 1, 2)
    plt.plot(carrier)
    plt.ylabel('Amplitude')
    plt.xlabel('Carrier signal')

    plt.subplot(3, 1, 3)
    plt.plot(result)
    plt.ylabel('Amplitude')
    plt.xlabel('Output signal')

    plt.show()

def main():
    stemplot()
    cosplot()
    fmMod()

if __name__ == '__main__':
    main()
