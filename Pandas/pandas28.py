# 28. Strip whitespace from string column.

import pandas as pd

data = {'Name': [' Abhi ', '  Vivi', 'John ']}

df = pd.DataFrame(data)

print(df)

df['Name'] = df['Name'].str.strip()

print(df)
