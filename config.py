import numpy as np

AREA_BOUNDS = (0, 100, 0, 100)

drone_positions = np.array([
    [20, 20],
    [80, 20],
    [50, 50],
    [20, 80],
    [80, 80],
])

drone_names = [f"DroneB_{i + 1}" for i in range(len(drone_positions))]

human_positions = np.array([
    [55, 60],
    [25, 30],
])