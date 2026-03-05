# 28. Normalize an array (scale 0–1).

import numpy as np

nums = np.array([2, 4, 6, 8, 10, 12, 5, 7, 12, 56, 3, 56])

min_val = np.min(nums)
max_val = np.max(nums)
    
if max_val == min_val:
    np.zeros_like(nums)
        
normalized = (nums - min_val) / (max_val - min_val)

print(normalized)