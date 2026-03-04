# 24. Fill missing values with forward fill.

import pandas as pd
import numpy as np

data = {'Col1': [54, 85, np.nan, 25, np.nan, 14],
        'Col2': [np.nan, 21, 85, np.nan, 96, 24]}

df = pd.DataFrame(data)

df = df.ffill() 

print(df)