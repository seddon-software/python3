from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# load iris data set
iris = load_iris()
X = iris.data
Y = iris.target

# define two unclassified iris's
iris1 = [4.1, 3.1, 1.8, 0.5]
iris2 = [6.9, 3.5, 3.5, 2.5]

def predict(estimator, message):
    estimator.fit(X, Y)     # train
    print(message, estimator.predict([iris1, iris2])) # estimate

# predict with different estimators and parameters
predict(KNeighborsClassifier(n_neighbors=1), "KNeighbors(K=1):")
predict(KNeighborsClassifier(n_neighbors=3), "KNeighbors(K=3):")
predict(KNeighborsClassifier(n_neighbors=5), "KNeighbors(K=5):")
predict(LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=150), "LogisticRegression:")
