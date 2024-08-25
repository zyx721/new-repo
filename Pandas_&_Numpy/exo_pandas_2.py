import pandas as pd

df = pd.read_csv("chapter_3_assets/2_dataframe_basics/Exercise/bengaluru_house_prices.csv")
print(df.shape)

print(df["area_type"].unique())
print(df["size"].unique())

print(df[(df["size"]=='2 BHK') &  (df["area_type"]=='Super built-up  Area')])
print(len(df[(df["size"]=='2 BHK') &  (df["area_type"]=='Super built-up  Area')]))

df["price_cateory"] = df.apply(lambda x : "Affordable" if x["price"]<80 else "High Cost",axis=1)

print(df[df["price"]>df["price"].mean()])