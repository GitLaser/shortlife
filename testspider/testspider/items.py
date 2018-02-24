# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class TestspiderItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()


class TaobaoItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()


class BoleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


def date_processor(time_string):
    return time_string.strip().rstrip(' ·')


class BoleItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    image = scrapy.Field()
    date = scrapy.Field(input_processor=MapCompose(date_processor))

    def get_insert_sql(self):
        sql = """
            insert into bole_article(title, image,  date,link)
            VALUES (%s, %s, %s, %s)
        """
        params = (self["title"], self["image"], self["date"], self["link"])
        return sql, params
