# -*-coding:utf8-*-
__datetime__ = "2017/12/25 21:13"
from sklearn.model_selection import train_test_split
from sklearn import datasets, tree
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_target = train_test_split(X, y, test_size=.5)
# print(X_train, X_test, y_train, y_target)
# clf = tree.DecisionTreeClassifier()
# my_classifier = clf.fit(X_train,y_train)
my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train,y_train)
my_predict = my_classifier.predict(X_test)
print(my_predict)
print(y_target)
print(accuracy_score(my_predict,y_target))