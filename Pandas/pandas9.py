# 9. Rename a column.

import pandas as pd

df = pd.read_csv("customers-100.csv")

print(df.columns[0])

df.rename(columns = {"Index" : "mainIndex"}, inplace = True)

print(df.columns[0])