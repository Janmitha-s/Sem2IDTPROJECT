import numpy as np

# Simulation parameters
fs = 1000          # Sampling frequency
duration = 60      # seconds
fc = 50            # Scaled-down carrier frequency

t = np.arange(0, duration, 1/fs)

tx_signal = np.cos(2 * np.pi * fc * t)

np.save("tx_signal.npy", tx_signal)
np.save("time.npy", t)

print("Transmitted signal generated.")