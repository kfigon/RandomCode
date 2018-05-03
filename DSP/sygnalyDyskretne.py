import matplotlib.pyplot as plt
import numpy as np
import math

def numpySin():
    x = np.arange(0, 10, 0.1)
    y = np.sin(2*np.pi* x)
    
    plt.plot(x,y)
    plt.xlabel('czas [t]')
    plt.ylabel('sin(x)')
    plt.title('numpy generated')
    plt.show()

def ownGeneratedSin():
    x = [i*0.1 for i in range(int(10/0.1))]
    y = [math.sin(2*3.1415*t) for t in x]

    plt.plot(x,y)
    plt.xlabel('czas [t]')
    plt.ylabel('sin(x)')
    plt.title('my generated')
    plt.show()

numpySin()
ownGeneratedSin()