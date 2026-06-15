import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

fs = 1000

doppler = np.load("doppler.npy")

f, t, Sxx = spectrogram(
    doppler,
    fs=fs,
    nperseg=2048,
    noverlap=1024
)

plt.figure(figsize=(10,6))

plt.pcolormesh(
    t,
    f,
    10*np.log10(Sxx + 1e-12),
    shading='gouraud'
)

plt.ylim(0,5)

plt.ylabel("Frequency (Hz)")
plt.xlabel("Time (s)")
plt.title("Micro-Doppler Spectrogram")

plt.colorbar(label="Power (dB)")
plt.savefig("spectrogram.png")
print("Spectrogram saved.")