# -*- coding: utf-8 -*-
import scrapy


class ZuihaodaxueSpider(scrapy.Spider):
    name = 'zuihaodaxue'
    allowed_domains = ['zuihaodaxue.com']
    start_urls = ['http://www.zuihaodaxue.com/']

    def parse(self, response):
        pass
