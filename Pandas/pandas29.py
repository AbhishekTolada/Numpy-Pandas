# 29. Convert string column to datetime.

import pandas as pd

df = pd.read_csv("orders.csv")

df["date"] = pd.to_datetime(df["date"])

print(df["date"])