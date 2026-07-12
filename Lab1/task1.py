import random
import time
import matplotlib.pyplot as plt

# sorting algorithms
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
    """In-place Lomuto partition scheme, last element as pivot."""
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


#timing helper
def time_it(func, data):
    start = time.perf_counter()
    func(data)
    return (time.perf_counter() - start) * 1000  # ms


#benchmark
random.seed(7)
full_data = [random.randint(0, 100000) for _ in range(10000)]
test_sizes = list(range(1000, 10001, 1000))

algorithms = {
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
}

results = {name: [] for name in algorithms}

for size in test_sizes:
    sample = full_data[:size]
    print(f"Benchmarking size = {size}")
    for name, func in algorithms.items():
        results[name].append(time_it(func, sample))

print("\nExecution Times (ms)")
for i, size in enumerate(test_sizes):
    row = " | ".join(f"{name}={results[name][i]:8.2f}" for name in algorithms)
    print(f"{size:5d} | {row}")

#plot
plt.figure(figsize=(12, 7))
for name, times in results.items():
    plt.plot(test_sizes, times, marker='o', label=name)
plt.title("Sorting Algorithm Performance")
plt.xlabel("Number of Elements")
plt.ylabel("Execution Time (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("snapshots/task1_output.png", dpi=150)
plt.show()