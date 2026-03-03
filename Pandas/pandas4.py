# Display first 5 rows.

import pandas as pd

df = pd.read_csv("D:\Downloads\customers-100.csv")

print(df.head(5))