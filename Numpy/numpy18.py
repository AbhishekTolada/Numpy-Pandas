# 18. Modify a slice of an array.

import numpy as np

nums = np.array([2, 4, 6, 8, 10, 12, 5, 7, 12, 56, 3, 56])

nums[1:5:2] = 100

print(nums)