# 34. Stack two arrays vertically.

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

stack = np.vstack((a, b))

print(stack)