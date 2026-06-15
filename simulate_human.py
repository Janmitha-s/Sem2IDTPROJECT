import numpy as np

t = np.load("time.npy")

# Human vital signs
breathing_freq = 0.3   # Hz
heartbeat_freq = 1.2   # Hz

breathing_amp = 0.01   # meters
heartbeat_amp = 0.001

displacement = (
    breathing_amp * np.sin(2*np.pi*breathing_freq*t)
    + heartbeat_amp * np.sin(2*np.pi*heartbeat_freq*t)
)

np.save("displacement.npy", displacement)

print("Human motion generated.")