import numpy as np

# ─────────────────────────────
# 1. Data Generation
# ─────────────────────────────
sales = np.random.randint(low=1000, high=9000, size=12)

# ─────────────────────────────
# 2. Basic Stats
# ─────────────────────────────
average = np.mean(sales)
med = np.median(sales)
standard = np.std(sales)
variance = np.var(sales)

# ─────────────────────────────
# 3. Min / Max
# ─────────────────────────────
minimum = np.min(sales)
maximum = np.max(sales)

# ─────────────────────────────
# 4. Percentiles
# ─────────────────────────────
percen = np.percentile(sales,[25,50,75]).astype(int)

# 5. Normalization (0-1)
normalized = (sales - minimum) / (maximum - minimum)

# ─────────────────────────────
# 6. Summary
# ─────────────────────────────
print("=" * 35)
print("     SALES STATS SUMMARY")
print("=" * 35)
print("Mean:", average)
print("Median:", med)
print("Std:", standard)
print("Variance:", variance)
print("minimum sales ",minimum)
print("maximum sales ",maximum)
print("percentile range ",percen)
print("Normalization value:")
for i, val in enumerate(np.round(normalized, 2)):
    print(f"  Month {i+1}: {val}")