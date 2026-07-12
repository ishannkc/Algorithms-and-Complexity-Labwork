import random
import time
import matplotlib.pyplot as plt


#sorting algorithms
def selection_sort(data):
    a = data[:]
    n = len(a)
    for start in range(n):
        lowest = start
        for scan in range(start + 1, n):
            if a[scan] < a[lowest]:
                lowest = scan
        a[start], a[lowest] = a[lowest], a[start]
    return a


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


def _merge(left, right):
    merged = []
    li = ri = 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            merged.append(left[li])
            li += 1
        else:
            merged.append(right[ri])
            ri += 1
    merged.extend(left[li:])
    merged.extend(right[ri:])
    return merged


def merge_sort(data):
    if len(data) <= 1:
        return data[:]
    mid = len(data) // 2
    return _merge(merge_sort(data[:mid]), merge_sort(data[mid:]))


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
sizes = list(range(50, 501, 50))
trials = 15

algorithms = {
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
}

profiles = {name: {"Best": [], "Average": [], "Worst": []} for name in algorithms}

for size in sizes:
    print(f"Benchmarking size = {size}")
    sorted_data = list(range(size))          # best case: already sorted
    reversed_data = list(range(size, 0, -1))  # worst case: reverse sorted

    for name, func in algorithms.items():
        best_total = sum(time_it(func, sorted_data) for _ in range(trials))

        worst_total = sum(time_it(func, reversed_data) for _ in range(trials))

        avg_total = 0
        for _ in range(trials):
            random_data = random.sample(range(size * 10), size)
            avg_total += time_it(func, random_data)

        profiles[name]["Best"].append(best_total / trials)
        profiles[name]["Average"].append(avg_total / trials)
        profiles[name]["Worst"].append(worst_total / trials)

#plot chart for algorithms
for name in algorithms:
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, profiles[name]["Best"], marker='o', color='green', label='Best Case')
    plt.plot(sizes, profiles[name]["Average"], marker='s', color='blue', label='Average Case')
    plt.plot(sizes, profiles[name]["Worst"], marker='x', color='red', label='Worst Case')
    plt.title(f"{name} Performance Profile")
    plt.xlabel("Array Size (N)")
    plt.ylabel("Execution Time (ms)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"snapshots/task2_{name.replace(' ', '_')}.png", dpi=150)
    plt.show()