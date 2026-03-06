# 40. Use fancy indexing to select specific columns.

import numpy as np

arr = np.array([
    [10, 11, 12],
    [20, 21, 22],
    [30, 31, 32],
    [40, 41, 42]
])

print(arr[:, [1, 2]])