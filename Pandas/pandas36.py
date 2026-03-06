# 36. Filter groups based on condition.

import pandas as pd
import numpy as np

data = {'Subject': ['A', 'A', 'A', 'B', 'B', 'C', 'C'],
        'Visit': ['foo', 'bar', 'baz', 'foo', 'cream', 'foo', 'bar']}
df = pd.DataFrame(data)

filtered_df_contains = df.groupby('Subject').filter(lambda x: x['Visit'].str.contains('cream').any())

print(filtered_df_contains)