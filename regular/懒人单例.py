# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/9 15:45"


# class Lazy:
#     __instance = None
#     def __init__(self):
#         if not Lazy.__instance:
#             print('__init__ method called...')
#         else:
#             print('instance %s created' % Lazy.__instance)
#     @classmethod
#     def getIns(cls):
#         if not cls.__instance:
#             cls.__instance = Lazy
#         return cls.__instance
#
#     def whoami(self):
#         print(self.__class__)
# dog = Lazy()
# dog.whoami()
#
# print(Lazy.getIns())
# cat = Lazy()

class LazySingle:
    __ins = None

    def __init__(self):
        if not LazySingle.__ins:
            print('initiate instance')
        else:
            print('instance exist',self.getIns())

    @classmethod
    def getIns(cls):
        if not cls.__ins:
            cls.__ins = LazySingle()
        return cls.__ins


today = LazySingle()
tomorrow = LazySingle()
print(id(today),id(tomorrow))