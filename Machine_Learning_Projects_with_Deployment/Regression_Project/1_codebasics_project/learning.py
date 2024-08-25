import pickle
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X ,y = fetch_openml('mnist_784',version=1,return_X_y=True)
x1,x2,y1,y2 = train_test_split(X ,y,train_size=0.8)
clf = RandomForestClassifier(n_jobs=1)
clf.fit(x1,y1)
print(clf.score(x2,y2))
with open('mnist_model.pkl','wb') as f :
    pickle.dump(clf,f)