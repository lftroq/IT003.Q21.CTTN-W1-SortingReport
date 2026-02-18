'''
Author: lftroq
Description: Sort arrays using numpy sort in Python.
'''
import numpy as np
import time
import sys
from pathlib import Path

# === CONFIG ===
N_ARRAY = 10
N_FLOAT = N_ARRAY // 2

DATASET_DIR = Path("../dataset")
LOG_FILE = Path("../time.txt")

def validation(array: np.ndarray) -> bool:
    if np.any(array[1:] < array[:-1]):
        i = int(np.argmax(array[1:] < array[:-1])) + 1
        print(f"Sort failed at index #{i}:\narray[{i}]: {array[i]}\narray[{i-1}]: {array[i-1]}")
        return False
    return True

def main():
    times_ms = []

    for i in range(1, N_ARRAY + 1):
        path = DATASET_DIR / f"array_{i}.npy"
        if not path.exists():
            print(f"Missing file: {path}")
            sys.exit(1)

        data = np.load(path)

        start = time.perf_counter()
        sorted_data = np.sort(data, kind='mergesort')
        elapsed = time.perf_counter() - start

        ms = int(elapsed * 1000)
        times_ms.append(ms)
        print(f"Time taken in #{i} array: {elapsed:.6f} seconds")

        if not validation(sorted_data):
            print(f"Validation failed for array #{i}.")
            sys.exit(1)

    LOG_FILE.write_text(" ".join(map(str, times_ms)) + " ")
    print(f"Logged to {LOG_FILE}")

if __name__ == "__main__":
    main()
