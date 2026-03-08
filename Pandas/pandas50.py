import pandas as pd

df = pd.read_csv("EmployeeAttrition.csv")

df.drop_duplicates

print(df)