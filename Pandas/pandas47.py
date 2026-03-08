# 47. Use map() to transform values

import pandas as pd

data = {'item': ['apple', 'banana', 'cherry', 'apple', 'date']}
df = pd.DataFrame(data)

fruit_to_color = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

df['color'] = df['item'].map(fruit_to_color)

print(df)