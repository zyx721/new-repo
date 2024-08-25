import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn

df = pd.read_csv("heights.csv")

print(df.height.describe())

# sn.histplot(df['height'], kde=True).set(
#     title='Height Distribution with KDE',
#     xlabel='Height',
#     ylabel='Frequency'
# )

# plt.show()
mean = df.height.mean()
std = df.height.std()
m1 = mean - 3*std
m2 = mean + 3*std
print(df[(df.height > m2) | (df.height < m1)])
df_clean = df[(df.height < m2) & (df.height > m1)]
print(df_clean.shape)
print(df.shape)
df['zscore'] = (df.height - df.height.mean())/df.height.std()

df = df[(df.zscore > -3) & (df.zscore < 3)]
print(df.shape)
#exercice
df = pd.read_csv("bhp.csv")
print(df.price_per_sqft.describe())
percentile_999 = df['price_per_sqft'].quantile(0.999)
percentile_001 = df['price_per_sqft'].quantile(0.001)
ndf = df[(df.price_per_sqft < percentile_999) & (df.price_per_sqft > percentile_001)]
print(ndf.shape)
print(df.shape)

m1 = ndf.price_per_sqft.mean() - ndf.price_per_sqft.std()*4
m2 = ndf.price_per_sqft.mean() + ndf.price_per_sqft.std()*4
df['zscore'] = (ndf.price_per_sqft - ndf.price_per_sqft.mean())/ndf.price_per_sqft.std()
newdf = df[(df.zscore > -4) & (df.zscore < 4)]
print(newdf.shape)
plt.hist(ndf.price_per_sqft,bins=20, rwidth=0.8,density=True)
plt.show()