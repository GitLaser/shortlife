# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/4 15:31"
import time
# def log(func):
#     def show_log(*args,**kwargs):
#         print("Call %s" % func.__name__)
#         return func(*args,**kwargs)
#     return show_log
#
# @log
# def time_now():
#     print(time.ctime())
#
# time_now()

def log(txt):
    def deco(func):
        def show_log(*args,**kwargs):
            print("txt: %s,Call: %s" % (txt,func.__name__))
            return func(*args,**kwargs)
        return show_log
    return deco

@log('2018年1月4日 南京暴雪黄色警报')
def showtime():
    print(time.ctime())

showtime()