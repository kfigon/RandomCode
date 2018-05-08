import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

step = 0.01
fs = 1/step
time = np.arange(0, 10, step)

f1 = 1
sin1 = np.sin(2*3.1415*f1 * time)

f2 = 4
sin2 = np.sin(2*3.1415*f2 * time)

added = sin1+sin2



order, cutoff = 6, f1/(fs*0.5)
b, a = signal.butter(order, cutoff, btype='low', analog=False)
filtrowany = signal.lfilter(b, a, added)

plt.subplot(2,1,1)
plt.plot(time, added)

plt.subplot(2,1,2)
plt.plot(time, filtrowany)
plt.show()
