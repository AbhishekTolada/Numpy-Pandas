# 22. Count missing values per column.

import pandas as pd

df = pd.read_excel("Customer Call List.xlsx")

print(df.isnull().sum())