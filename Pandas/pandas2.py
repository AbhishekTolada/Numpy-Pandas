# Create a DataFrame from dictionary.

import pandas as pd

data = {
        "Name" : ["Abhi", "Vivi", "John"],
        "Age" : ["10", "20", "30"],
        "City" : ["vizag", "hyderabad", "USA"]
}

new_data = pd.DataFrame(data)

print(new_data)