# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/2/9 21:53"
#乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d" % (j,i,i*j),end='\t')
#     print()

#求可用被17整除的所有三位数
# for i in range(100,1000):
#     if i % 17 ==0:print(i)

#写一个程序，提示输入整数X，然后计算从1到X连续整数的和
# def summ(x):
#     print(sum(range(0,x)))
# summ(10)

#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

# from itertools import permutations
# resumt = permutations([1,2,3,4],3)
# for each in resumt:
#     print(each)


#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# import math
#
# num = 1
# while True:
#     if math.sqrt(num + 100)-int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268)-int(math.sqrt(num + 268)) == 0:
#         print(num)
#         break
#     num += 1

#题目：输入某年某月某日，判断这一天是这一年的第几天？

# import datetime
# first_day = datetime.datetime.strptime("2018-01-01","%Y-%m-%d")
# print(first_day)
#
# today = datetime.datetime.today()
# print(today)
#
# print((today-first_day).days+1)




