# -*-coding:utf8 -*-
from copy import deepcopy

__author__ = "陈子昂"
__datetime__ = "2018/1/21 15:58"

l1 = [1,2]
l2=[3,4,l1]
# l3=l2.copy()
l3=deepcopy(l2)
l1.append('a')
print(l3)

def ge():
    for i in range(5):
        yield 'ok'+str(i)

a=ge()
print(next(a))
print(next(a))
print(next(a))

