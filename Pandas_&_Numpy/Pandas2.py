import pandas as pd
# df = pd.read_csv("stock_data.csv",skiprows=0,names=[""])
# df = pd.read_csv("stock_data.csv",header=1)
# # print(df)
# # df = pd.read_csv("stock_data.csv",header=1,na_values={
# #     "eps":['not available'],"revenue":[-1],"people":['not available','n.a.']
# # })
#
# # df = pd.read_csv("stock_data.csv",header=1,na_values={['not available',-1,'n.a.']})
# df["price"] = pd.to_numeric(df["price"], errors='coerce')
# df["eps"] = pd.to_numeric(df["eps"], errors='coerce')
# df['pe'] = df['price'] / df['eps']
# print(df)
# # df.to_csv("pe1.csv",index=False,header=False)
# df2 = pd.read_excel('movies_db.xlsx',"movies")
# print(df2.head(4))
# def standardize_currency(curr):
#     if curr == "$$" or curr == "Dollars":
#         return "USD"
#     return curr
#
# dff = pd.read_excel('movies_db.xlsx',"financials",converters={'currency': standardize_currency} )
# print(dff)
# pm=pd.merge(df2,dff,on="movie_id")
# print(pm)
# pm.to_excel("movies_meged.xlsx",sheet_name="marged",index=False)
#
# df_stocks = pd.DataFrame({
# 'tickers': ['GOOGL', 'NMT', 'MSFT'],
# 'price': [845, 65, 64 ],
# 'pe': [30.37, 14.26, 39.97],
# 'eps': [27.82, 4.61, 2.12]
# })
# df_weather = pd.DataFrame({
#     'day':['1/1/2017','1/2/2017','1/3/2017'],
#     'temperature':[32,35,28],
#     'event':['Rain','sunny','snow']
# })
# with pd.ExcelWriter("stocks_weather.xlsx") as writer:
#     df_stocks.to_excel(writer, sheet_name="stocks")
#     df_weather.to_excel(writer, sheet_name="weather")

#exercice:
p = pd.read_csv("movies_data.csv")
print(p.head(5))

p["year_classify"] =p.apply(lambda x: 'Before 2000'if x['release_year']<2000 else 'from 2000',axis=1)
print(p)
p.to_csv("final_movie_data.csv",columns=["movie_id","title","budget","revenue","year_classify"],index=False)