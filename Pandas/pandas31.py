# 31. Group by one column and compute mean.

import pandas as pd

df = pd.read_csv("age_income.csv")

mean = df.groupby('age')['income'].mean()

print(mean)