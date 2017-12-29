# -*-coding:utf8-*-
__datetime__ = "2017/12/19 22:57"
import numpy as np
import pydot
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz
from sklearn.externals.six import StringIO
iris = load_iris()
test_idx = [0, 50, 100]

# training data
# print(iris.target)
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#test data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]


clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)
print(test_target)
print(clf.predict(test_data))

# viz code
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")
dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
