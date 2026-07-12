# COMP 314 - Algorithms & Complexity

This repository contains the labwork implementations for the coursework of COMP 314 (Algorithms & Complexity). Contains all implementation code for each lab work.

## Lab 1: Sorting Algorithm Analysis

### Task 1: Comparative Analysis of Sorting Algorithms
Selection, Insertion, Merge, Quick and Heap sort are benchmarked on random datasets of increasing size and their execution times are plotted.

### Task 2: Best, Average and Worst Case Analysis
Each sorting algorithm is run on sorted (best), random (average) and reverse-sorted (worst) input, and a separate performance-profile chart is produced for each algorithm.

### Task 3: Insertion Sort vs Heap Sort (Best Case)
The best-case performance of Insertion Sort and Heap Sort is compared using already-sorted input arrays ranging from 1,000 to 10,000 elements.

### Task 4: Activity Selection Problem
A brute-force recursive algorithm and a greedy algorithm are compared to illustrate exponential vs near-linear (n log n) growth.

### Task 5: Quick Sort Performance Analysis
Quick Sort (Lomuto partition, last-element pivot) is tested on random input (best/average case) and already-sorted input (worst case) to show the effect of pivot selection on performance.

## Folder Structure

```
(Algorithms & Complexity)/
├── .gitignore
├── README.md
└── Lab1/
    ├── task1.py
    ├── task2.py
    ├── task3.py
    ├── task4.py
    ├── task5.py
    └── snapshots/
        ├── task1_output.png
        ├── task2_Heap_Sort.png
        ├── task2_Insertion_Sort.png
        ├── task2_Merge_Sort.png
        ├── task2_Quick_Sort.png
        ├── task2_Selection_Sort.png
        ├── task3_output.png
        ├── task4_output.png
        └── task5_output.png
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/ishannkc/Algorithms-and-Complexity-Labwork
cd Algorithms-and-Complexity-Labwork
```

### Prerequisites
- Python 3.x
- matplotlib

```bash
pip install matplotlib
```