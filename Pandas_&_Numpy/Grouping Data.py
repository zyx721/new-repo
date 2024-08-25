import pandas as pd
# a = pd.read_csv("chapter_3_assets/6_group_by/weather_by_cities.csv")
# b = a.groupby("city")
# # for c , d in b:
# #     print("city: ",c)
# #     print("\n")
# #     print("max: ",d.temperature.max())
# print(b.describe())
# def foo(a,x,col):
#     if 80<= a[col].loc[x]<=90:
#         return '80-90'
#     elif 50<= a[col].loc[x]<=60:
#         return '56'
#     else:
#         return 'others'
# c = a.groupby(lambda x : foo(a,x,'temperature'))
# for l,l2 in c:
#     print(l)
#     print(l2)
#exercice:
p = pd.read_csv("chapter_3_assets/6_group_by/Exercise/movies_data.csv")
print(p)

g = p.groupby('industry')

print(g.size())
# print(g.get_group('Bolywood'))
def grouper(df, idx, col):
    if 1 <= df[idx].loc[col] <= 3.9 :
        return 'p'
    elif 4 <= df[idx].loc[col] <= 7.9:
        return 'a'
    elif 8 <= df[idx].loc[col] <= 10:
        return 'Good'
    else:
        return "others"
g = p.groupby(lambda x: grouper(p, x, 'imdb_rating'))
for key, d in g:
    print(key)
    print(d)