# 19. Remove duplicate rows.

import pandas as pd

df = pd.read_excel("Customer Call List.xlsx")

df = df.drop_duplicates()

print(df)