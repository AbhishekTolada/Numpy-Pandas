# 47. Find duplicate values in array.

import numpy as np

a = np.array([1, 2, 1, 3, 3, 3, 0, 4, 2])

unq, c = np.unique(a, return_counts=True)

duplicates = unq[c > 1]

print(duplicates)