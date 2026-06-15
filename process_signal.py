import numpy as np
from scipy.signal import butter, filtfilt

tx = np.load("tx_signal.npy")
rx = np.load("received.npy")

mixed = tx * rx

fs = 1000

b, a = butter(4, 3/(fs/2), btype='low')

doppler = filtfilt(b, a, mixed)

np.save("doppler.npy", doppler)

print("Doppler extracted.")