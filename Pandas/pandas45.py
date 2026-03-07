# 45. Apply custom function to column.

import pandas as pd

df = pd.read_csv("age_income.csv")

print(df["age"].apply(lambda x: x+10))