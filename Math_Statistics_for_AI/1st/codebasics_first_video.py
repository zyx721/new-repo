import numpy as np
import pandas as pd

df = pd.read_csv("income.csv")

print(df.describe())

p99 = df["Monthly Income ($)"].quantile(0.99)

df_nooutlier = df[df["Monthly Income ($)"] <= p99]

print(df_nooutlier)

df.loc[3, "Monthly Income ($)"] = np.nan
print(df)

df = df.fillna(df["Monthly Income ($)"].median())
print(df)

#exercice
df2 = pd.read_csv("AB_NYC_2019.csv")
print(df2)

df2["reviews_per_month"] = df2["reviews_per_month"].fillna(df2["reviews_per_month"].median())

min_threshold, max_threshold = df2["price"].quantile([0.01, 0.999])

print(df2.price.describe())

df2 = df2[(df2["price"] <= max_threshold) & (df2["price"] >= min_threshold)]

print(df2.price.describe())