# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/4 13:45"

# def counter():
#     def f():
#         n=0
#         while True:
#             n+=1
#             yield n
#     s = f()
#     def n():
#         return next(s)
#     return n


# def counter():
#     f=[0]
#     def h():
#         f[0]+=1
#         return f[0]
#     return h


def counter():
    i=0
    def h():
        nonlocal i
        i+=1
        return i
    return h
a=counter()
print(a(),a(),a())

