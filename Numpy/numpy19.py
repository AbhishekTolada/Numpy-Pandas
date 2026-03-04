# 19. Use boolean masking to filter data.

import numpy as np

nums = np.array([2, 4, 6, 8, 10, 12, 5, 7, 12, 56, 3, 56])

nums = nums[nums > 10]

print(nums)