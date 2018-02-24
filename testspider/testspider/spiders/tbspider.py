# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/2/2 14:00"
import scrapy
import re
from scrapy.http import Request
from testspider.items import TaobaoItem
class TestSpider(scrapy.Spider):
    """
        name:scrapy唯一定位实例的属性，必须唯一
        allowed_domains：允许爬取的域名列表，不设置表示允许爬取所有
        start_urls：起始爬取列表
        start_requests：它就是从start_urls中读取链接，然后使用make_requests_from_url生成Request，
                        这就意味我们可以在start_requests方法中根据我们自己的需求往start_urls中写入
                        我们自定义的规律的链接
        parse：回调函数，处理response并返回处理后的数据和需要跟进的url
        log：打印日志信息
        closed：关闭spider
        """
    # 设置name
    name = 'taobao'
    allowed_domains = ["taobao.com"]
    start_urls = ['http://taobao.com']

    def parse(self, response):
        key = '小吃'
        for i in range(0, 2):
            url = 'https://s.taobao.com/search?q=' + str(key) + '&s=' + str(44 * i)
            # print(url)
            yield Request(url=url, callback=self.page)

    def page(self, response):
        body = response.body.decode('utf-8', 'ignore')
        pattam_id = '"nid":"(.*?)"'
        all_id = re.compile(pattam_id).findall(body)
        # print(all_id)
        for i in range(0, len(all_id)):
            this_id = all_id[i]
            url = 'https://item.taobao.com/item.htm?id=' + str(this_id)
            yield Request(url=url, callback=self.next)

    def next(self, response):
        url = response.url
        pattam_url = 'https://(.*?).com'
        subdomain = re.compile(pattam_url).findall(url)
        # print(subdomain)
        if subdomain[0] != 'item.taobao':
            title = response.xpath("//div[@class='tb-detail-hd']/h1/text()").extract()

        else:
            title = response.xpath("//h3[@class='tb-main-title']/@data-title").extract()


        print(title)
