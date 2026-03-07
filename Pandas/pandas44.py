# 44. Find rows present in one DataFrame but not in another.

import pandas as pd

df1 = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5, 3], 'col2': [10, 11, 12, 13, 14, 10]})
df2 = pd.DataFrame(data={'col1': [1, 2, 3], 'col2': [10, 11, 12]})

print(pd.concat([df1, df2]).drop_duplicates(keep=False))