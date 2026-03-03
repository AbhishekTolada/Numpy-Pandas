# 15. Extract all elements greater than 50.

import numpy as np

arr = np.array([90, 45, 100, 34, 55])

for val in arr:
    if val>50:
        print(val, end = " ")