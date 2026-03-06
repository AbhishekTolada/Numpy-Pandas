# 35. Find department with highest average salary.

import pandas as pd

df = pd.read_csv("employee.csv")

dept = df.groupby("Department")["Salary"].max()

print(dept.idxmax())