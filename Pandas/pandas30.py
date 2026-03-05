# 30. Extract year from datetime column.

import pandas as pd

df = pd.read_csv("orders.csv")

df["date"] = pd.to_datetime(df["date"])

df["date"] = df["date"].dt.year

print(df["date"])