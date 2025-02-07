import numpy as np

arr = np.random.rand(100) * 100  
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("Original Array:")
print(arr)
print("\nNormalized Array:")
print(normalized_arr)