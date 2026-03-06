# 35. Stack two arrays horizontally.

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

stack = np.hstack((a, b))

print(stack)