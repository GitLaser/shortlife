# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/9 23:26"


# 用元类创建类
# class MyMeta(type):
#     x=1
#     def __call__(self):
#         print('call MyMeta----')
#
# MyCls = MyMeta('MyCls',(MyMeta,),{'X':'2'})

# 元类的单例实现
class MetaSingle(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingle,cls).__call__(*args,**kwargs)
        return cls.__instance

class logger(metaclass=MetaSingle):
    pass

log1 = logger
log2 = logger
print(log1,log2)
print(id(log1),id(log2 ))
