# Practical 4: 0/1 Knapsack (Dynamic Programming)
import matplotlib.pyplot as plt

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
n = len(weights)

dp = [[0] * (capacity + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

# Backtracking selected items
w, selected = capacity, []
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(i)
        w -= weights[i - 1]

print(f"Weights: {weights} | Values: {values} | Capacity: {capacity}")
print(f"Max Value: ${dp[n][capacity]} | Selected Items: {selected[::-1]}")

plt.figure(figsize=(8, 3.5))
plt.imshow(dp, cmap="YlGnBu", aspect="auto")
plt.colorbar(label="Value ($)")
plt.title("0/1 Knapsack: DP Table (Items vs Capacity)")
plt.xlabel("Capacity (0 to 50)"); plt.ylabel("Item Index (0 to 3)")
plt.tight_layout()
plt.show()