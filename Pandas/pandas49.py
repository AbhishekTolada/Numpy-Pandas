import pandas as pd

df = pd.read_csv("sales.csv")

total = df["Total Profit"].sum()
monthly = total/12

print("Total Revenue is:", total)

print("Monthly Revenue is:", monthly)

dropped_columns = ["Total Units", "Total Profit"]

df = df.drop(["Total Units", "Total Profit", "Month"], axis=1)

print("Best selling product is:", df.columns.max())

# print(df)

column_sums = df.sum()

top_3_column_names = column_sums.sort_values(ascending=False).head(3).index.tolist()

df_top_3_columns = df[top_3_column_names]

print(df_top_3_columns)