# -*- coding: utf-8 -*-
import scrapy
from testspider.items import BoleItem,BoleItemLoader
from scrapy.http import Request
from urllib import parse
class BoleSpiderSpider(scrapy.Spider):
    name = 'bole'
    allowed_domains = ['python.jobbole.com']
    start_urls = ['http://python.jobbole.com/all-posts/']

    def parse(self, response):
        # 获取当前页所有文章的url
        article_nodes = response.xpath('//*[@id="archive"]/div/div')
        for node in article_nodes:
            article_url = node.xpath('./a/@href').extract_first('')
            # image_url = node.xpath('./a/img/@scr').extract_first('')
            image= 'www.zenofpy.cn'
            yield Request(url=parse.urljoin(response.url,article_url),meta={'image':image},callback=self.parse_detail)

        # next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        # if next_url:
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)


    def parse_detail(self,response):
        item_loader = BoleItemLoader(item=BoleItem(),response=response)
        image = response.meta.get('image','')
        item_loader.add_value('image',image)
        item_loader.add_xpath('title','//div[@class="entry-header"]/h1/text()')
        item_loader.add_xpath('date','//div[@class="entry-meta"]/p/text()')
        item_loader.add_value('link',response.url)

        article_item = item_loader.load_item()
        yield article_item
