# 46. Create new column based on condition.

import pandas as pd
import numpy as np

data = {'Score': [7.884, 6.952, 8.185, 6.556, 6.347, 6.794]}

df = pd.DataFrame(data)

df["Result"] = np.where(df["Score"] >= 7.0, 'Pass', 'Fail')

print(df)
