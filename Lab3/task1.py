import time
import matplotlib.pyplot as plt
from functools import lru_cache

# -----------------------------
# Recursive Fibonacci
# -----------------------------
def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# -----------------------------
# Dynamic Programming Fibonacci
# -----------------------------
@lru_cache(maxsize=None)
def dp_fibonacci(n):
    if n <= 1:
        return n
    return dp_fibonacci(n - 1) + dp_fibonacci(n - 2)

# Test values
n_values = list(range(1, 36))

recursive_times = []
dp_times = []

# Average over multiple runs
runs = 5

for n in n_values:

    # Recursive
    total = 0
    for _ in range(runs):
        start = time.perf_counter()
        recursive_fibonacci(n)
        total += time.perf_counter() - start
    recursive_times.append(total / runs)

    # Dynamic Programming
    total = 0
    for _ in range(runs):
        dp_fibonacci.cache_clear()
        start = time.perf_counter()
        dp_fibonacci(n)
        total += time.perf_counter() - start
    dp_times.append(total / runs)

# Plot
plt.figure(figsize=(10,6))

plt.plot(
    n_values,
    recursive_times,
    linewidth=2.5,
    marker='o',
    markersize=4,
    label='Recursive Fibonacci'
)

plt.plot(
    n_values,
    dp_times,
    linewidth=2.5,
    marker='s',
    markersize=4,
    label='Dynamic Programming Fibonacci'
)

plt.title("Recursive Fibonacci vs Dynamic Programming Fibonacci")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()