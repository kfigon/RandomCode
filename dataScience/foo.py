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


def main():
    stemplot()
    cosplot()


if __name__ == '__main__':
    main()