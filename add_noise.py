import numpy as np

tx = np.load("tx_signal.npy")
disp = np.load("displacement.npy")

wavelength = 0.33

phase_shift = (4 * np.pi * disp) / wavelength

reflection = np.cos(np.angle(tx + 1j*0) + phase_shift)

noise = np.random.normal(0, 0.3, len(reflection))

received = reflection + noise

np.save("received.npy", received)

print("Reflection with noise generated.")