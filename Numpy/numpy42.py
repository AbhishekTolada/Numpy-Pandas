# 42. Create a checkerboard pattern matrix.

import numpy as np

def board(n):
    matrix = np.array([[0, 1], [1, 0]])
    checker = np.tile(matrix, (n//2, n//2))
    return checker

print(board(5))