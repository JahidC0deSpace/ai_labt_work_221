import numpy as np

matrix = np.random.randint(1, 101, (5, 5))
row_sums = np.sum(matrix, axis=1)

print("Generated 5x5 Matrix:")
print(matrix)
print("\nRow-wise Sums:")
print(row_sums)
