# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/21 20:39"

import  sys
import requests


test_url = sys.argv[1]
# print(test_url)
# test_url = "https://item.jd.com/5089225.html"
api_url = 'http://pricecomparison.browser.qq.com/get_comparison_info'
ss = requests.session()
headers = {
    'Host':'pricecomparison.browser.qq.com',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12918.400',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
params = {'url':test_url}
res = ss.request(method='GET',url=api_url,headers=headers,params=params,verify=False)
js = res.json()

price = js['price']['currentprice']
is_store = js['product'][0]['storelevel']

# 根据storelevel货存状态就行了，时间关系 没弄

print('售价：%s，货存状态：%s' % (price,is_store)) #storelevel






