# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/2/21 14:31"

import time, threading

def say(n):
    print('狗年旺旺%s' % n)
    print(threading.current_thread().name)
t1 = threading.Thread(target=say,args=['asd'],name='dsada')
t1.start()
t1.join()
print(threading.current_thread().name)