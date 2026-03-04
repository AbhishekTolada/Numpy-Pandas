# 25. Drop rows with missing values.

import pandas as pd
import numpy as np

data = {'A': [34, 58, np.nan, 15],
        'B': [23, np.nan, np.nan, 52],
        'C': [98, 35, 86, 23]}

df = pd.DataFrame(data)

print(df)

df.dropna(inplace=True)

print(df)