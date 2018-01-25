# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/21 14:33"

# 连续os，os.path
import os
import time
file_path = __file__
print(os.path.dirname(file_path))
print(os.path.basename(file_path))
print(os.path.join('C:/','Desktop'))
print(os.path.split(file_path))
print(os.path.splitext(file_path))
access_time = os.path.getatime(file_path)
english_time = time.ctime(access_time)
print("本文件访问时间："+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(access_time)))
print("本文件大小："+os.path.getsize(file_path).__str__())
print(os.path.isabs(file_path))
print(os.path.isfile(file_path),os.path.isdir(file_path))
