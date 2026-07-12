def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp, dp[n][capacity]


def print_table(dp):
    print("\nDP Table (rows = items used, columns = capacity 0..W)")
    for row in dp:
        print(" ".join(f"{val:3}" for val in row))


# Main Program
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    v = int(input(f"Enter value of item {i + 1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter knapsack capacity: "))

dp, max_value = knapsack(weights, values, capacity)

print_table(dp)
print("\nMaximum value that fits in the knapsack:", max_value)