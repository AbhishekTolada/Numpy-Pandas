# 14. Replace all even numbers with 0.

import numpy as np

arr = np.array([7, 3, 5, 7, 9, 2, 1, 4, 7, 9, 4, 5, 6, 3, 2, 1, 3, 4])

idx = 0 #index

for val in arr:
    if(val%2 == 0):
        arr[idx] = 0
    idx += 1

print(arr)