'''
Author: lftroq
Description: Run and benchmark sorting algorithms implemented in C++ and Python.
'''
import math
import os
import subprocess
import csv
import platform
import numpy as np

# === CONFIG ===
FOLDER_ALGO = "SortAlgorithms"
INPUT_DATA = "arrays.txt" 
TEMP_TIME_FILE = "time.txt"
OUTPUT_CSV = "result.csv"

CPP_ALGOS = ["cppsort", "heapsort", "mergesort", "quicksort"]
PY_ALGOS = ["numpysort.py"]

def compile_cpp():
    # === COMPILING C++ ===
    print("=== Compiling C++ files ===")
    
    exe_ext = ".exe" if platform.system() == "Windows" else ""
    
    for algo in CPP_ALGOS:
        cpp_file = os.path.join(FOLDER_ALGO, f"{algo}.cpp")
        exe_file = os.path.join(FOLDER_ALGO, f"{algo}{exe_ext}")
        
        if not os.path.exists(cpp_file):
            print(f"Could not find file: {cpp_file}")
            continue

        cmd = ["g++", cpp_file, "-o", exe_file, "-O2"]
        
        try:
            subprocess.check_call(cmd)
            print(f"Compiled: {algo}")
        except subprocess.CalledProcessError:
            print(f"Could not compile: {algo}")

def parse_time_file():
    try:
        if not os.path.exists(TEMP_TIME_FILE):
            return None, None, None

        with open(TEMP_TIME_FILE, "r") as f:
            lines = f.readlines()

        raw_str = lines[0].strip().split()
        raw_times = [float(x) for x in raw_str]

        mean_val = mean_val = sum(raw_times) / len(raw_times)
        variance = sum((x - mean_val) ** 2 for x in raw_times) / (len(raw_times) - 1)
        std_val = math.sqrt(variance)

        return raw_times, mean_val, std_val

    except Exception as e:
        print(f"Error while reading {TEMP_TIME_FILE}: {e}")
        return None, None, None

def run_algorithms():
    results = []
    
    csv_header = ["Algorithm"] + [f"Run {i+1}" for i in range(10)] + ["Mean", "Std Dev"]
    results.append(csv_header)

    exe_ext = ".exe" if platform.system() == "Windows" else ""

    # Run C++ algorithms
    for algo in CPP_ALGOS:
        print(f"Running: {algo}...")
        exe_path = os.path.join(FOLDER_ALGO, f"{algo}{exe_ext}")
        
        if os.path.exists(exe_path):
            try:
                subprocess.run([os.path.abspath(exe_path)], cwd=FOLDER_ALGO, check=True)
                raw_times, mean, std = parse_time_file()
                
                if raw_times:
                    row = [algo] + raw_times + [mean, std]
                    results.append(row)
                else:
                    print(f"Cannot read data from time.txt for {algo}")
            except Exception as e:
                print(f"Error while running {algo}: {e}")
        else:
            print(f"Cannot find executable for {algo}")

    # Run Python algorithm
    for py_algo in PY_ALGOS:
        print(f"Running: {py_algo}...")
        py_path = os.path.join(FOLDER_ALGO, py_algo)
        
        if os.path.exists(py_path):
            try:
                subprocess.run(["python", py_algo], cwd=FOLDER_ALGO, check=True)
                
                raw_times, mean, std = parse_time_file()
                if raw_times:
                    row = [py_algo] + raw_times + [mean, std]
                    results.append(row)
            except Exception as e:
                print(f"Error while running {py_algo}: {e}")

    # 3. GHI FILE CSV
    try:
        with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(results)
        print(f"\nDone! Results saved to '{OUTPUT_CSV}'")
    except Exception as e:
        print(f"Error writing CSV file: {e}")

def main():
    # Kiểm tra file input
    if not os.path.exists(INPUT_DATA):
        print(f"Could not find file '{INPUT_DATA}' at root directory!")
        print("Make sure the C++ code points to the correct path (usually ../arrays.txt)")

    compile_cpp()
    run_algorithms()

if __name__ == "__main__":
    main()