# 34. Find highest salary per department.

import pandas as pd

df = pd.read_csv("employee.csv")

print(df.groupby("Department")["Salary"].max())