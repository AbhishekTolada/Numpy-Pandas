# 16. Select first column of a 2D array.

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

data = arr[:, 0]

print(data)