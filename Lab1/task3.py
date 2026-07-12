import time
import matplotlib.pyplot as plt


def insertion_sort(data):
    a = data[:]
    for pos in range(1, len(a)):
        value = a[pos]
        spot = pos
        while spot > 0 and a[spot - 1] > value:
            a[spot] = a[spot - 1]
            spot -= 1
        a[spot] = value
    return a


def _sift_down(a, root, size):
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < size and a[left] > a[largest]:
            largest = left
        if right < size and a[right] > a[largest]:
            largest = right
        if largest == root:
            break
        a[root], a[largest] = a[largest], a[root]
        root = largest


def heap_sort(data):
    a = data[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(a, i, n)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        _sift_down(a, 0, end)
    return a


def time_it(func, data):
    start = time.perf_counter()
    func(data)
    return (time.perf_counter() - start) * 1000


#benchmark
sizes = list(range(1000, 10001, 1000))
trials = 100

insertion_times = []
heap_times = []

for size in sizes:
    print(f"Benchmarking best-case size = {size} (averaging {trials} trials)")
    sorted_data = list(range(size))

    insertion_total = sum(time_it(insertion_sort, sorted_data) for _ in range(trials))
    heap_total = sum(time_it(heap_sort, sorted_data) for _ in range(trials))

    insertion_times.append(insertion_total / trials)
    heap_times.append(heap_total / trials)

print("\nBest-Case Execution Times (ms)")
print(f"{'Size':<7} | {'Insertion Sort':<16} | {'Heap Sort':<10}")
print("-" * 40)
for i, size in enumerate(sizes):
    print(f"{size:<7} | {insertion_times[i]:<16.4f} | {heap_times[i]:<10.4f}")

#plot
plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_times, marker='o', color='green', linewidth=2.5, label='Insertion Sort (Best Case)')
plt.plot(sizes, heap_times, marker='s', color='blue', linewidth=2.5, label='Heap Sort (Best Case)')
plt.title("Best-Case Comparison: Insertion Sort vs Heap Sort")
plt.xlabel("Number of Elements (N)")
plt.ylabel("Average Execution Time (ms)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("snapshots/task3_output.png", dpi=150)
plt.show()