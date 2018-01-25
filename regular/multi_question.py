# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/21 20:36"


with open('demo.txt') as f:
    txt_list = f.read().split('\n')
    txt_set = set(txt_list)
    for each in txt_set:
        k,v = each.split(' ')
        print('%s：%s,%d;' %(k,v,txt_list.count(each)))






 
