# 43. Concatenate horizontally.

import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df2 = pd.DataFrame({
    'C': [7, 8, 9],
    'D': [10, 11, 12]
})

print(pd.concat([df1, df2], axis=1))