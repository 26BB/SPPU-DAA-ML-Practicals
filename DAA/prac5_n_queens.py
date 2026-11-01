# Practical 5: N-Queens Problem (Backtracking)
import numpy as np, matplotlib.pyplot as plt

n = 4

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1: return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1: return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1: return False
    return True

solutions = []
def solve(board, row):
    if row == n:
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, row + 1)
            board[row][col] = 0

board = [[0] * n for _ in range(n)]
solve(board, 0)

print(f"Total Solutions for N={n}: {len(solutions)}")
print(f"Solution 1 Board:\n" + "\n".join([" ".join(["Q" if x else "." for x in r]) for r in solutions[0]]))

# Plot Chessboard
checkered = np.indices((n, n)).sum(axis=0) % 2
fig, ax = plt.subplots(figsize=(4, 4))
ax.imshow(checkered, cmap="binary", alpha=0.3)
for r in range(n):
    for c in range(n):
        if solutions[0][r][c] == 1:
            ax.text(c, r, "Q", fontsize=20, ha="center", va="center", color="red", fontweight="bold")
ax.set_xticks(range(n)); ax.set_yticks(range(n))
ax.set_title(f"{n}-Queens Placement")
plt.tight_layout()
plt.show()
