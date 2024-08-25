import  pandas as pd
# india_weather = pd.DataFrame({
# "city": ["mumbai","delhi","banglore"],
# "temperature": [32,45,30],
# "humidity": [80, 66, 78]
# })
# us_weather = pd.DataFrame({
# "city": ["new york","chicago","orlando"],
# "temperature": [21,14,35],
# "humidity": [68, 65, 75]
# })
# a = pd.concat([india_weather,us_weather],keys=["indias","us"])
# print(a.loc["indias"])
#
# temperature_df = pd.DataFrame({
# "city": ["mumbai","delhi","banglore"],
# "temperature": [32,45,39],
# })
#
# windspeed_df = pd.DataFrame({
# "city": ["delhi","mumbai"],
# "windspeed": [7,12],
# },index=[1,0])
#
# print(pd.concat([temperature_df,windspeed_df],axis=1))
# import pandas as pd
#
# df1 = pd.DataFrame({
# "city": ["new york","chicago","orlando"],
# "temperature": [21,14,35],
#
# })
#
# df2 = pd.DataFrame({
# "city": ["chicago","new york","orlando","s"],
# "humidity": [65,68,75,12],
# })
# print(pd.merge(df1,df2,on="city",how="outer"))
#exercice:
m = pd.read_csv("chapter_3_assets/7_concat_merge/Exercise/movies.csv")
f = pd.read_csv("chapter_3_assets/7_concat_merge/Exercise/financials.csv")
l = pd.read_csv("chapter_3_assets/7_concat_merge/Exercise/languages.csv")
nm = pd.read_csv("chapter_3_assets/7_concat_merge/Exercise/new_movies.csv")
print(m.head(3))
print(f.head(3))
print(l.head(3))

m = pd.concat([m,nm],ignore_index=True)
print(m.tail(5))

m = pd.merge(m,l,on="language_id",how="inner")
print(m.head(5))

m =pd.merge(m,f,on="movie_id",how="left")
print(m.tail(5))

m.to_csv("final_complete_data7.csv",columns=["movie_id","title","lang_name","budget","revenue","currency"],index=False)