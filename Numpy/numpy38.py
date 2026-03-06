# 38. Multiply each column by a different number.

import numpy as np

arr1 = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

arr2 = np.array([10, 20, 30])

arr3 = np.diag(arr2)

print(arr1 @ arr3)