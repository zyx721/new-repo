import pickle
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
df = pd.read_csv('homeprices.csv')
print(df)

plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')
# plt.show()

price = df.price
print(price)
area = df["area"]
print(area)
new_df = df.drop('price',axis='columns')
print(new_df)
reg = linear_model.LinearRegression()
reg.fit(new_df,price)

print(reg.predict([[2600]]))
print(reg.coef_)
print(reg.intercept_)

area_df = pd.read_csv("areas.csv")
p = reg.predict(area_df)
area_df['price'] = p
print(area_df)
# area_df.to_csv("prediction.csv")

# with open('model_pickle','wb') as file:
#     pickle.dump(reg,file)
with open('model_pickle','rb') as file:
    mp = pickle.load(file)
print(mp.coef_)

import joblib
# joblib.dump(reg, 'model_joblib')

mj = joblib.load('model_joblib')