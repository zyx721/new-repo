import numpy as np
import pandas as pd
# df = pd.read_csv("chapter_3_assets/5_handling_missing_data_replace/weather_data.csv")
# df.replace([-99999,-88888],np.nan,inplace=False)
# print(df)
# df.replace({
#     'temperature':-99999,
#     'windspeed':[-99999,-88888],
#     'event' :'no event'
# },np.nan,inplace=False)
# print(df)
# df.replace({
#     -99999:np.nan,
#     -88888:np.nan,
#     'no event':'Sunny'
# },inplace=True)
# print(df)
# df = pd.DataFrame({
# 'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
# 'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
#
# })
# print(df)
# df.replace(['poor','average','good','exceptional'],[1,2,3,4],inplace=True)
# print(df)

#exercice
a = pd.read_csv("chapter_3_assets/5_handling_missing_data_replace/Exercise/food_db.csv")
print(a.shape)
print(a)

new_df = a.replace(["10%","5%"],"13%")
print(new_df)

new_df = a.replace( {'Excellent': 4, 'very Good': 3, 'Good': 2,
'Average': 1},regex=True)
print(new_df)