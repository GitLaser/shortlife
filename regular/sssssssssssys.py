# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/21 14:59"
import sys
print(sys.modules.keys())
a = 'a'
b=a

print(sys.getrefcount('a'))

