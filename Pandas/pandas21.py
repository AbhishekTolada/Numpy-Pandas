# 21. Detect missing values.

import pandas as pd

df = pd.read_excel("Customer Call List.xlsx")

print(df.isnull())