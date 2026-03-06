# 32. Group by multiple columns.

import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'A'],
    'Subcategory': ['one', 'one', 'two', 'two', 'one', 'two', 'one', 'two'],
    'Sales': [100, 150, 50, 200, 120, 180, 90, 60],
    'Quantity': [1, 2, 1, 3, 2, 1, 3, 2]
}

df = pd.DataFrame(data)

df = df.groupby(['Category', 'Subcategory']).sum()

print(df)