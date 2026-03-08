# 49. Compute correlation between two arrays.

import numpy as np

arr1 = np.array([6, 21, 37, 51])
arr2 = np.array([1, 25, 51, 75])

print(np.corrcoef(arr1, arr2))