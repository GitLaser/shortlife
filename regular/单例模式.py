# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/9 15:37"

class Single:

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Single,cls).__new__(cls)
        return cls.instance

A = Single()
print(id(A))
B = Single()
print(id(B))



