# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/4 21:30"

from enum import Enum,unique


# @unique
# class Season(Enum):
#     Spring = 1
#     Summer = 2
#     Autumn = 3
#     Winter = 4
# print(Season(1)==Season['Spring'])
Person = type('Person',(object,),dict(say='asdsadsda'))
a = Person
print(a.say)








