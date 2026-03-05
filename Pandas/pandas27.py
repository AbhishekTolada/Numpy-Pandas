# 27. Change datatype of column.

import pandas as pd

df = pd.read_csv("age_income.csv")

print(df["age"].dtype)

df["age"] = df["age"].astype(float)

print(df["age"].dtype)

print(df)