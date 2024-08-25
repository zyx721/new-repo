import pandas as pd
a =pd.read_csv("chapter_3_assets/4_handling_missing_data_fillna_dropna_interpolate/weather_data.csv",parse_dates=["day"])
print(type(a.day[0]))
a.set_index('day',inplace=True)
a.fillna(0)
a.fillna({
    'temperature':a.temperature.mean(),
    'windspeed': a.windspeed.mean(),
    'event':'No Event'
})
# a.fillna(method='bfill')
# a.interpolate(inplace=True)
print(a.dropna())
print(a.dropna(how='all'))
print(a.dropna(thresh=2))
#exercice
print("/ exercice ")
b = pd.read_csv("chapter_3_assets/4_handling_missing_data_fillna_dropna_interpolate/Exercises/fruits_data.csv")
print(b.shape)
print(b.columns)
print(b)

new_df = b.fillna('-1')
print(new_df)
new_df = b.fillna({
    'apple(1kg)':b["apple(1kg)"].mean(),
    'banana(1 dozen)':b['banana(1 dozen)'].mean(),
    'grapes(1kg)':b['grapes(1kg)'].median(),
    'mango(1kg)' : b['mango(1kg)'].median(),
    'Water Melons(1)':"Not Available"
},)
print(new_df)

new_df = b.fillna(method="ffill")
print(new_df)

new_df = b.dropna(thresh=4)
print(new_df)

new_df = b.dropna()
new_df.to_csv('final_data.csv',index=False)