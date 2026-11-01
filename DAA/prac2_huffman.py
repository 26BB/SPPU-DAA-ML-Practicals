# Practical 2: Huffman Encoding (Greedy)
import heapq, matplotlib.pyplot as plt
from collections import Counter

text = "BCAADDDCCACACAC"
freq = Counter(text)

heap = [[f, [ch, ""]] for ch, f in freq.items()]
heapq.heapify(heap)

while len(heap) > 1:
    left, right = heapq.heappop(heap), heapq.heappop(heap)
    for item in left[1:]: item[1] = "0" + item[1]
    for item in right[1:]: item[1] = "1" + item[1]
    heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

codes = {ch: code for ch, code in heap[0][1:]}
encoded = "".join(codes[ch] for ch in text)
savings = (1 - len(encoded) / (len(text) * 8)) * 100

print(f"Text: \"{text}\" | Unique Chars: {len(freq)}")
print(f"Huffman Codes: {codes}")
print(f"Encoded Bits: {len(encoded)} bits | Storage Saved: {savings:.2f}%")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))
ax1.bar(freq.keys(), freq.values(), color="mediumseagreen")
ax1.set_title("Frequencies"); ax1.set_ylabel("Count")

ax2.bar(codes.keys(), [len(c) for c in codes.values()], color="coral")
ax2.set_title("Code Length (Bits)"); ax2.set_ylabel("Bits")

plt.tight_layout()
plt.show()
