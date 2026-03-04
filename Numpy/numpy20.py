# 20. Find indices where elements are greater than a value.

import numpy as np

nums = np.array([2, 4, 6, 8, 10, 12, 5, 7, 12, 56, 3, 56])

print("index of the element greater than the value: ", end = "")

idx = 0

for val in nums:
    if(val > 5):
        print(idx, end = " ")
    idx += 1