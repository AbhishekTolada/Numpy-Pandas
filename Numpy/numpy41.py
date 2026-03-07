# 41. Replace negative values with 0 using vectorization.

import numpy as np

arr = np.array([-2, 1, -5, 4, 0, -3])

arr[arr < 0] = 0

print(arr)