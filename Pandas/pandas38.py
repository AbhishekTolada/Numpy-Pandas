# 38. Create pivot table.

import pandas as pd
import numpy as np

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Product': ['One', 'One', 'Two', 'Two', 'One', 'One', 'Two', 'Two'],
    'Sales': [10, 20, 15, 25, 12, 18, 16, 22],
    'Region': ['East', 'East', 'West', 'West', 'East', 'East', 'West', 'West']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

pivot_table = pd.pivot_table(
    data=df,
    values='Sales',
    index=['Category', 'Product'],
    columns='Region',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='Grand Total'
)

print("\nPivot Table:")
print(pivot_table)
