# 15. Select rows by index using iloc.

import pandas as pd

df = pd.read_csv("age_income.csv")

print(df.iloc[3])