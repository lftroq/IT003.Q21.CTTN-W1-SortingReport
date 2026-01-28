'''
Author: lftroq
Description: Sort arrays using numpy sort in Python.
'''
import numpy as np
import time
import sys

# === CONFIG ===
N_ARRAY = 10
LENGTH_EACH_ARRAY = int(1e6)
N_FLOAT = N_ARRAY // 2

INPUT_FILE = '../arrays.txt'
LOG_FILE = '../time.txt'

# === VALIDATION ===

def validation(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            print(f'Sort failed at index #{i}:\narray[{i}]: {array[i]}\narray[{i - 1}]: {array[i - 1]}')
            return False
    return True
    
def main():
    with open(INPUT_FILE, 'r') as f:
        arrays = f.readlines()

    with open(LOG_FILE, 'w') as log_f:
        for i in range(N_ARRAY):
            data_str = arrays[i].strip().split(' ')
            if i < N_FLOAT:
                data = np.array([float(x) for x in data_str], dtype=np.float64)
            else:
                data = np.array([int(x) for x in data_str], dtype=np.int64)

            start_time = time.time()
            sorted_data = np.sort(data)
            end_time = time.time()

            elapsed_time = end_time - start_time
            log_f.write(f'{int(elapsed_time * 1000)} ')
            print(f'Time taken in #{i + 1} array: {elapsed_time:.6f} seconds')

            if not validation(sorted_data):
                print(f'Validation failed for array #{i + 1}.')
                sys.exit(1)
if __name__ == "__main__":
    main()