# Generate 10 arrays, first 5 of them have 1.000.000 floats, last 5 of them have 1.000.000 integers.
import random as rd

N_ARRAY = 10
N_FLOAT = N_ARRAY // 2
N_INTS = N_ARRAY - N_FLOAT
LENGTH_EACH_ARRAY = int(1e6)
PATH = "arrays.txt"

def genData():
    with open(f"{PATH}", 'w') as f:
        print(f"Generating arrays to {PATH}...")

        for i in range(N_FLOAT):
            data = []
            for cnt in range(LENGTH_EACH_ARRAY):
                data.append(rd.uniform(-1000000000, 1000000000))

            if i == 0: # Sort first array increasing
                data.sort()
            elif i == 1: # Sort second array decreasing
                data.sort(reverse=True)

            # Write array to file
            for x in data:
                f.write(str(x) + ' ')
            f.write('\n')
            print(f"Float array #{i + 1} generated, first 5 elements:", data[:5])

        for i in range(N_INTS):
            data = []
            for cnt in range(LENGTH_EACH_ARRAY):
                data.append(rd.randint(-1000000000, 1000000000))
            for x in data:
                f.write(str(x) + ' ')
            f.write('\n')
            print(f"Integer array #{i + 1} generated, first 5 elements:", data[:5])

        print("Generating completed.")
        return data

genData()
