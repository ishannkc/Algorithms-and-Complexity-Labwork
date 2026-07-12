import time
import random
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(5000)

def quick_sort(data):
    a = data[:]

    def partition(lo, hi):
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    def sort(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            sort(lo, p - 1)
            sort(p + 1, hi)

    sort(0, len(a) - 1)
    return a


def time_it(func, data):
    start = time.perf_counter()
    func(data)
    return (time.perf_counter() - start) * 1000


#benchmark
sizes = list(range(100, 1501, 100))
trials = 30

best_case_times = []
worst_case_times = []

print("Running Quick Sort benchmarks...")
for size in sizes:
    print(f"Benchmarking size = {size}")
    best_sum = 0
    worst_sum = 0
    for _ in range(trials):
        random_data = [random.randint(0, 100000) for _ in range(size)]
        sorted_data = list(range(size))

        best_sum += time_it(quick_sort, random_data)
        worst_sum += time_it(quick_sort, sorted_data)

    best_case_times.append(best_sum / trials)
    worst_case_times.append(worst_sum / trials)


#plot
plt.figure(figsize=(10, 6))
plt.plot(sizes, best_case_times, marker='o', color='green', linewidth=2.5,
         label='Best Case (Random Data)')
plt.plot(sizes, worst_case_times, marker='x', color='red', linewidth=2.5,
         label='Worst Case (Sorted Data)')
plt.title("Quick Sort Performance Analysis: Best vs. Worst Case")
plt.xlabel("Number of Elements (N)")
plt.ylabel("Average Execution Time (ms)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("snapshots/task5_output.png", dpi=150)
plt.show()