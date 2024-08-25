import pandas as pd

df = pd.read_csv("movies.csv")
print(df.industry.unique())
print(df.head(0))
print(df.language.value_counts())
print(df[["title","industry"]])
# print(df[df.release_year>2000 & (df.release_year<2010)])
print(df.studio.unique())
print(df.describe())
print(df.info())

print(df[(df.imdb_rating==df.imdb_rating.max()) | (df.imdb_rating==df.imdb_rating.min())])
df["age"] = df['release_year'].apply(lambda x:2024 - x)
df["profit"] = df.apply(lambda x:x['revenue']- x['budget'],axis=1)

df.set_index("title",inplace=True)
print(df.loc["Pather Panchali"])
df.reset_index(inplace=True)
# print(df.inloc["2:4"])
print(df)
# print(df.tail(1))
# print(df.sample(1))
# print(df[2:3])
# print(df.shape)
# print(max(df.imdb_rating))
# print(dir(df.imdb_rating))
# print(df.imdb_rating.min(),df.imdb_rating.max(),df.imdb_rating.mean())
# print(df[df.industry=="Hollywood"].imdb_rating.min())







# import csv
#
#
# def calculate_rating_stats(data, industry=None):
#     ratings = []
#     for row in data:
#         if row[3] != 'NULL' and (not industry or row[1] == industry):
#             ratings.append(float(row[3]))
#     max_rating = max(ratings)
#     min_rating = min(ratings)
#     avg_rating = sum(ratings) / len(ratings)
#     return max_rating, min_rating, avg_rating
#
#
# with open('movies.csv') as f:
#     data = list(csv.reader(f))
#     header = data[0]
#     data = data[1:]
#
#     max_rating, min_rating, avg_rating = calculate_rating_stats(data)
#     print(f"All records: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")
#
#     max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Bollywood")
#     print(f"Bollywood: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")
#
#     max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Hollywood")
#     print(f"Hollywood: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")
