# 46. Set random seed and generate reproducible output

import numpy as np

np.random.seed(100) 

arr = np.random.rand(5)

print(arr)