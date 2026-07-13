# COMP 314 - Algorithms & Complexity

This repository contains the labwork implementations for the coursework of **COMP 314 (Algorithms & Complexity)**. Contains all implementation code for each lab work.

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

## Lab 2: Algorithm Design Paradigms

### Task 1: 0/1 Knapsack (Dynamic Programming)
A DP solution to the 0/1 knapsack problem using a 2D table where rows represent items and columns represent capacities (0 to W), returning the maximum attainable value.

### Task 2: Karger's Minimum Cut (Randomized Algorithm)
An implementation of Karger's randomized contraction algorithm for undirected graphs. Edges are contracted at random until two vertices remain; the smallest cut across multiple trials is reported.

### Task 3: Parallel Merge Sort (Parallel Computing)
Merge sort parallelised with `multiprocessing.Pool`. The array is split in half and each half is sorted concurrently in separate processes before merging.

### Task 4: DPLL SAT Solver (Backtracking / SAT)
A recursive DPLL solver for 3-CNF propositional formulas using unit propagation and backtracking to decide satisfiability and produce a satisfying assignment.

## Lab 3: Advanced Algorithms

### Task 1: Recursive Fibonacci vs Dynamic Programming Fibonacci
Compares the exponential recursive Fibonacci (O(2ⁿ)) against memoized DP Fibonacci (O(n)). Both approaches are benchmarked on n = 1 to 35 and their execution times are plotted to demonstrate the dramatic speedup from dynamic programming.

### Task 2: Connected Components — Sequential vs Parallel DFS
Finds connected components in an undirected graph using sequential DFS (O(V+E)) and parallel DFS via `ThreadPoolExecutor` (O((V+E)/P)). The user specifies the number of vertices and processors; the program generates a random graph, runs both approaches, and plots the theoretical complexity curves.

## Folder Structure

```
(Algorithms & Complexity)/
├── .gitignore
├── README.md
├── Lab1/
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   ├── task4.py
│   ├── task5.py
│   └── snapshots/
│       ├── task1_output.png
│       ├── task2_Heap_Sort.png
│       ├── task2_Insertion_Sort.png
│       ├── task2_Merge_Sort.png
│       ├── task2_Quick_Sort.png
│       ├── task2_Selection_Sort.png
│       ├── task3_output.png
│       ├── task4_output.png
│       └── task5_output.png
├── Lab2/
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   └── task4.py
└── Lab3/
    ├── task1.py
    └── task2.py
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