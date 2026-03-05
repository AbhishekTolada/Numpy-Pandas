# 26. Replace specific values.

import pandas as pd

df = pd.read_csv("age_income.csv")

df.loc[df['age'] < 60, 'age'] = 1

print(df)