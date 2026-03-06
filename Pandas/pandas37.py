# 37. Use transform() to compare row with group average.

import pandas as pd

data = {
    'Group': ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C'],
    'Value': [10, 14, 3, 4, 9, 20, 19, 21, 24]
}

df = pd.DataFrame(data)

df['Group_Average'] = df.groupby('Group')['Value'].transform('mean')

df['Difference_from_Average'] = df['Value'] - df['Group_Average']

print(df)