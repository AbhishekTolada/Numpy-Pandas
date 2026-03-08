# 48. Rank values within group.

import pandas as pd

df = pd.DataFrame({
    'group': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'name': ['p2382', 'p9183', 'p1253', 'p3382', 'p5583', 'p1211', 'p0482', 'p7374', 'p2382'],
    'score': [7.55, 3.22, 5.77, 2.11, 1.22, 0.77, 8.55, 8.21, 7.77]
})

df['rank'] = df.groupby('group')['score'].rank(ascending=False, method='min')

print(df.sort_values(by=['group', 'rank']))