# Practical 1: Fibonacci Numbers (Iterative vs Recursive)
import matplotlib.pyplot as plt

n = 10

# Iterative Approach
def fib_iter(num):
    a, b, res = 0, 1, []
    for _ in range(num):
        res.append(a)
        a, b = b, a + b
    return res

# Recursive Approach
rec_count = 0
def fib_rec(k):
    global rec_count
    rec_count += 1
    return k if k <= 1 else fib_rec(k - 1) + fib_rec(k - 2)

iter_res = fib_iter(n)
calls = []
for i in range(n):
    rec_count = 0
    fib_rec(i)
    calls.append(rec_count)

print(f"Fibonacci Series (First {n} terms): {iter_res}")
print(f"Iterative Steps: {n - 1} | Recursive Calls for F({n - 1}): {calls[-1]}")

plt.figure(figsize=(7, 3.5))
plt.plot(range(n), range(n), marker="o", color="blue", label="Iterative O(N)")
plt.plot(range(n), calls, marker="s", color="red", label="Recursive O(2^N)")
plt.title("Fibonacci Complexity: Iterative vs Recursive")
plt.xlabel("N"); plt.ylabel("Operations"); plt.legend(); plt.grid(True)
plt.tight_layout()
plt.show()
