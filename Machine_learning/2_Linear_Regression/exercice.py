import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
df = pd.read_csv("canada_per_capita_income.csv")
print(df)
plt.xlabel("year")
plt.ylabel("income")
plt.scatter(df["year"],df["per capita income (US$)"],color='green',marker='*')
plt.plot(df.year,df["per capita income (US$)"])
plt.show()
d = df.drop("per capita income (US$)",axis='columns')
model = linear_model.LinearRegression()
model.fit(d,df["per capita income (US$)"],)
print(model.predict([[2020]]))
df.dr