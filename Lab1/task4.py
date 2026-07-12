import random
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(5000)


#brute-force
def brute_force_select(activities, index=0, last_end=-1):
    if index == len(activities):
        return 0, []

    skip_count, skip_list = brute_force_select(activities, index + 1, last_end)

    start, end = activities[index]
    if start >= last_end:
        take_count, take_list = brute_force_select(activities, index + 1, end)
        take_count += 1
        take_list = take_list + [(start, end)]
        if take_count > skip_count:
            return take_count, take_list

    return skip_count, skip_list


#greedy sort
def greedy_select(activities):
    ordered = sorted(activities, key=lambda act: act[1])
    chosen = []
    last_end = -1
    for start, end in ordered:
        if start >= last_end:
            chosen.append((start, end))
            last_end = end
    return chosen


#demo
demo_activities = [
    (1, 4), (3, 5), (0, 6), (5, 7), (3, 9),
    (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16),
]
print("--- Activity Selection Demonstration ---")
print(f"Total activities: {len(demo_activities)}")
print(f"Activities: {demo_activities}\n")

bf_count, bf_list = brute_force_select(demo_activities)
print(f"Brute force result ({bf_count} activities): {bf_list}")

g_list = greedy_select(demo_activities)
print(f"Greedy result ({len(g_list)} activities): {g_list}\n")


#benchmark
def time_it(func, arg):
    start = time.perf_counter()
    func(arg)
    return (time.perf_counter() - start) * 1000


max_n = 18
trials = 50

brute_times = []
greedy_times = []
n_values = list(range(1, max_n + 1))

for n in n_values:
    print(f"Benchmarking n = {n}")
    brute_sum = 0
    greedy_sum = 0
    for _ in range(trials):
        starts = [random.randint(0, 50) for _ in range(n)]
        acts = [(s, s + random.randint(1, 20)) for s in starts]

        brute_sum += time_it(lambda a: brute_force_select(a), acts)
        greedy_sum += time_it(greedy_select, acts)

    brute_times.append(brute_sum / trials)
    greedy_times.append(greedy_sum / trials)

#plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, brute_times, marker='o', color='#d62728', linewidth=2.5,
         label='Brute Force (Exponential: $O(2^n)$)')
plt.plot(n_values, greedy_times, marker='s', color='#1f77b4', linewidth=2.5,
         label='Greedy Approach ($O(n \\log n)$)')
plt.title("Activity Selection: Complexity Comparison")
plt.xlabel("Number of Activities (n)")
plt.ylabel("Execution Time (ms)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("snapshots/task4_output.png", dpi=150)
plt.show()