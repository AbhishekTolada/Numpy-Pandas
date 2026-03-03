# 14. Filter rows where salary between 50k–100k.

import pandas as pd

df = pd.read_csv("age_income.csv")

df = df[(df["income"] > 50000) & (df["income"] < 100000)]

print(df)