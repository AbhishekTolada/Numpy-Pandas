# 18. Sort by multiple columns.

import pandas as pd

df = pd.read_csv("age_income.csv")

df = df.sort_values(by=["income", "age"])

print(df)