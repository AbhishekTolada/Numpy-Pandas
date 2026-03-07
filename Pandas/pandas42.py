# 42. Concatenate two DataFrames vertically.

import pandas as pd

df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
df2 = pd.DataFrame({'Name': ['Charlie', 'David'], 'Age': [35, 40]})
df3 = pd.DataFrame({'Name': ['Eve', 'Frank'], 'Salary': [50000, 60000]})

print(pd.concat([df1, df2, df3], ignore_index=True))