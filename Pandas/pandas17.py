# 17. Sort by one column.

import pandas as pd

df = pd.read_csv("age_income.csv")

df = df.sort_values(by="age")

print(df)