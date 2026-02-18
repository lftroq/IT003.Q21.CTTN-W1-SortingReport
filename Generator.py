import numpy as np
import os

os.makedirs("dataset", exist_ok=True)

N_ARRAY = 10
LENGTH = 1_000_000

for i in range(5):
    a = np.random.uniform(-1e9, 1e9, LENGTH).astype(np.float64)
    if i == 0:
        a.sort()
    elif i == 1:
        a.sort()
        a = a[::-1]
    np.save(f"dataset/array_{i+1}.npy", a)

for i in range(5, 10):
    a = np.random.randint(-1e9, 1e9, LENGTH, dtype=np.int64)
    np.save(f"dataset/array_{i+1}.npy", a)
