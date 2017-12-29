# -*-coding:utf8-*-
__datetime__ = "2017/12/19 22:46"
from sklearn import tree
features =[[100,0],[120,0],[150,1],[160,1]] # 0 bumpy 1 smooth
labels = [0,0,1,1] #0 orange 1 apple
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[140,1]]))