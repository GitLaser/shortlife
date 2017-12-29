# -*-coding:utf8-*-
from random import choice

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

__datetime__ = "2017/12/25 21:55"

from scipy.spatial import distance
from sklearn.datasets import load_iris

iris = load_iris()


def euc(a, b):
    return distance.euclidean(a, b)


class SuanFa():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]


X = iris.data
y = iris.target
X_train, X_test, y_train, y_target = train_test_split(X, y, test_size=.5)
my_classifier = SuanFa()
my_classifier.fit(X_train=X_train, y_train=y_train)
predict_result = my_classifier.predict(X_test)

# print(y_target)

print(accuracy_score(predict_result, y_target))
