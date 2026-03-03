# 10. Drop a column.

import pandas as pd

df = pd.read_csv("customers-100.csv")

df.drop('Last Name', axis = 1, inplace = True)

print(df.columns)