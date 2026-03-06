# 39. Merge two DataFrames (inner join).

import pandas as pd

df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C', 'D'],
    'Value1': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'Key': ['B', 'D', 'E', 'F'],
    'Value2': [5, 6, 7, 8]
})

merge = pd.merge(df1, df2, on='Key', how='inner')

print(merge)