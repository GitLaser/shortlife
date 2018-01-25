# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/21 19:47"

#已知如下序列：[(1,{"date":"2015-3-1"},"jack"),(2,{"date":"2015-3-2"},"tom")...]，写程序根据date先后排序。


info_list = [(1,{"date":"2015-3-1"},"jack"),
             (2,{"date":"2015-3-3"},"tom"),
             (3,{"date":"2015-3-2"},"andy")]

new_list = sorted(info_list,key=lambda info:info[1]['date'])

print(new_list)