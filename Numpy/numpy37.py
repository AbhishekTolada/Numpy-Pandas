# 37. Subtract row mean from each row (broadcasting).

import numpy as np

arr1 = np.array([[5, 6, 7, 8],
              [1, 2, 3, 4],
              [9, 10, 11, 12]])

mean = np.mean(arr1, axis=1, keepdims=True)

arr2 = arr1 - mean

print(arr2)