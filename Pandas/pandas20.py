# 20. Get unique values of a column.

import pandas as pd

df = pd.read_excel("Customer Call List.xlsx")

df = df["Paying Customer"].unique()

print(df)