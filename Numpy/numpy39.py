# 39. Use fancy indexing to select specific rows.

import numpy as np

arr = np.array([
    [10, 11, 12],
    [20, 21, 22],
    [30, 31, 32],
    [40, 41, 42]
])

fancy_index = [3, 2, 1]

print(arr[fancy_index])