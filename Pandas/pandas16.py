# 16. Select rows by label using loc.

import pandas as pd

df = pd.read_csv("age_income.csv")

print(df.loc[3:])