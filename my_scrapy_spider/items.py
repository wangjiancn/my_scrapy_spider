# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    upc = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    review_rating = scrapy.Field()
    review_num = scrapy.Field()
    stock = scrapy.Field()


class JdItem(scrapy.Item):
    price = scrapy.Field()
    name = scrapy.Field()


class JobbleItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    praise = scrapy.Field()
    fav = scrapy.Field()
    comments = scrapy.Field()
    tag = scrapy.Field()
    web_address = scrapy.Field()

class MyScrapySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

