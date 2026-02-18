# IT003.Q21.CTTN-W1-SortingReport

A report and benchmarking project for **Sorting Algorithms** in the Data Structures & Algorithms course (UIT).  
This repository provides a complete pipeline to:

1. Generate datasets for testing
2. Benchmark different sorting implementations
3. Save results to CSV
4. Visualize performance using plots

This repository also includes a report as pdf file.

The project focuses on analyzing sorting performance on large datasets and comparing execution time across different algorithms.

---

## Requirements

- Python 3.x
- Libraries:
  - numpy
  - matplotlib

Install dependencies:

```bash
pip install numpy matplotlib
```

---

## Usage

### Generating dataset

Run:

```bash
python Generator.py
```

This script creates a `dataset/` folder containing **10 arrays**, each with **1,000,000 elements**:

- `array_1.npy`: sorted ascending (float64)
- `array_2.npy`: sorted descending (float64)
- `array_3.npy` ... `array_5.npy` — random float64 arrays
- `array_6.npy` ... `array_10.npy` — random int64 arrays

---

### Benchmarking

Run:

```bash
python Main.py
```

The pipeline will:

- Execute sorting scripts inside `SortAlgorithms/`.
- Measure sorting time for each dataset.
- Store temporary timings in `time.txt`.
- Compute mean and standard deviation.
- Export results to `result.csv`.

Algorithms benchmarked:

- Quick Sort
- Heap Sort
- Merge Sort
- NumPy Sort (library-based)

---

### Visualizing 

Run:

```bash
python Plot.py
```

This generates:

- Line chart showing runtime across datasets
- Bar chart showing mean and standard deviation
- An image that includes both charts.

---

## Output

- `result.csv` — raw benchmark statistics
- `SortingAnalysis.png` — performance visualization
- `SortingReport.pdf/.docx` — written report and analysis in Vietnamese

---

## Notes

- The algorithms in `SortAlgorithms/` currently rely on `numpy.sort(..., kind=...)` for benchmarking rather than fully manual implementations.
- `time.txt` is a temporary file and will be overwritten each run.
- The project is designed for **performance comparison**, not algorithm correctness testing.

---

## Author

- lftroq

---
