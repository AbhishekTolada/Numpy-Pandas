# 23. Fill missing values with mean.

import pandas as pd
import numpy as np

data = {'Col1': [34, 56, np.nan, 13, 96], 
        'Col2': [52, np.nan, 79, 85, 65]}

df = pd.DataFrame(data)

df.fillna(df.mean(numeric_only=True), inplace=True)

print(df)