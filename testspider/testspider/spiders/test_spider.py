# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/31 12:18"

import scrapy
from testspider.items import TestspiderItem

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
    name = 'test'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    def parse(self,response):
        for each in response.xpath('//*[@id="syncad_1"]/h1'):
            item = TestspiderItem()
            item['link'] = each.xpath('.//@href').extract()
            item['title'] = each.xpath('.//text()').extract()
            # print(item)
            yield item

