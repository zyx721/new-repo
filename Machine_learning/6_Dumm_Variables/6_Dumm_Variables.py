import pandas as pd

# Example dataframe
data = {'town': ['A', 'B', 'A', 'C']}
df = pd.DataFrame(data)

# Get dummies
dummies = pd.get_dummies(df.town)

print(dummies)