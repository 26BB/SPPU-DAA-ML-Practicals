# Practical 3: Fractional Knapsack (Greedy)
import matplotlib.pyplot as plt

capacity = 50
items = [("Item 1", 10, 60), ("Item 2", 20, 100), ("Item 3", 30, 120)] # (name, weight, value)
items.sort(key=lambda x: x[2] / x[1], reverse=True)

curr_cap, total_val, fractions = capacity, 0.0, []
for name, wt, val in items:
    if curr_cap >= wt:
        curr_cap -= wt
        total_val += val
        fractions.append(1.0)
    elif curr_cap > 0:
        frac = curr_cap / wt
        total_val += val * frac
        fractions.append(frac)
        curr_cap = 0
    else:
        fractions.append(0.0)

print(f"Knapsack Capacity: {capacity} | Items: {items}")
print(f"Max Value: ${total_val:.2f} | Fractions Taken: {fractions}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))
names = [x[0] for x in items]
ax1.bar(names, [x[2] / x[1] for x in items], color="royalblue")
ax1.set_title("Ratio (Value/Weight)"); ax1.set_ylabel("$/kg")

ax2.bar(names, [f * 100 for f in fractions], color="forestgreen")
ax2.set_title("Allocation %"); ax2.set_ylabel("Percentage Taken")
ax2.set_ylim(0, 110)

plt.tight_layout()
plt.show()