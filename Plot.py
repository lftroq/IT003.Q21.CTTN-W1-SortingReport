import matplotlib.pyplot as plt
import numpy as np
import csv
import os

INPUT_CSV = 'result.csv'

def load_data_from_csv(filename):
    # === LOAD DATA FROM CSV ===
    data = {}
    
    if not os.path.exists(filename):
        print(f"Error : File '{filename}' does not exist.")
        return {}

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)  
            
            if not header:
                return {}

            for row in reader:
                if not row: continue
                
                algo_name = row[0]
                try:
                    times = [float(x) for x in row[1:11]]
                    data[algo_name] = times
                except ValueError:
                    print(f"Error parsing times for {algo_name}, skipping this entry.")
                    continue
                    
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return {}
        
    return data

def draw_full_analysis():
    data = load_data_from_csv(INPUT_CSV)

    # === SETUP PLOT ===
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    markers = ['o', 's', '^', 'D', 'v']

    # === LINE PLOT ===
    run_indices = np.arange(1, 11)
    
    for i, (algo, times) in enumerate(data.items()):
        ax1.plot(run_indices, times, marker=markers[i], linestyle='-', 
                 linewidth=2, label=algo, color=colors[i])

    ax1.set_title('Execution Time per Run (1-10)', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Run Index (Input Data Variation)', fontsize=12)
    ax1.set_ylabel('Time (ms)', fontsize=12)
    ax1.set_xticks(run_indices)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend()

    # === BAR PLOT ===
    algos = list(data.keys())
    means = [np.mean(v) for v in data.values()]
    std_devs = [np.std(v, ddof=1) for v in data.values()]

    bars = ax2.bar(algos, means, yerr=std_devs, capsize=10, 
                   color=colors, alpha=0.9, edgecolor='grey', width=0.6)

    ax2.set_title('Mean Time & Standard Deviation', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Algorithm', fontsize=12)
    ax2.set_ylabel('Time (ms)', fontsize=12)
    ax2.grid(axis='y', linestyle='--', alpha=0.6)

    for bar, mean, std in zip(bars, means, std_devs):
        height = bar.get_height()
        label = f'{mean:.1f}\n±{std:.1f}'
        ax2.text(bar.get_x() + bar.get_width()/2, height + std + 10, 
                 label, ha='center', va='bottom', fontsize=10, fontweight='bold')

    # === SAVE AND SHOW ===
    plt.tight_layout()
    plt.savefig('SortingAnalysis.png')
    plt.show()

if __name__ == "__main__":
    draw_full_analysis()