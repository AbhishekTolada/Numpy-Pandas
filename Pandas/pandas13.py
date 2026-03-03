# 13. Filter rows where age > 30.

import pandas as pd

df = pd.read_csv("age_income.csv")

df = df[df["age"]>30]

print(df)