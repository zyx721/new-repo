from sklearn.metrics.pairwise import cosine_similarity, cosine_distances
import pandas as pd

print(cosine_similarity([[3,1]],[[6,2]]))
print(cosine_distances([[3,1]],[[6,2]]))
print(cosine_similarity([[3,100]],[[6,2]]))


df = pd.DataFrame([
        {'iPhone': 3,'galaxy': 1},
        {'iPhone': 2,'galaxy': 0},
        {'iPhone': 1,'galaxy': 3},
        {'iPhone': 1,'galaxy': 2},
    ],
    index=[
        "doc1",
        "doc2",
        "doc3",
        "doc4"
    ])
print(df)

print(cosine_similarity(df.loc["doc1":"doc1"],df.loc["doc2":"doc2"]))
print(cosine_similarity(df.loc["doc1":"doc1"],df.loc["doc4":"doc4"]))
print(cosine_distances(df.loc["doc1":"doc1"],df.loc["doc4":"doc4"]))
print(1 - cosine_similarity(df.loc["doc1":"doc1"],df.loc["doc4":"doc4"]))