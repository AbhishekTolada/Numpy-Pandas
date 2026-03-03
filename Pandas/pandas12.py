# 12. Select multiple columns.

import pandas as pd

df = pd.read_csv("customers-100.csv")

print(df.loc[:, "Index":"Email"])