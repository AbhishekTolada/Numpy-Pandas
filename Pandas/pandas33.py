# 33. Calculate sum, mean, count together.

import pandas as pd

df = pd.read_csv("age_income.csv")

print(df)

print(df.agg(['sum', 'mean', 'count']))