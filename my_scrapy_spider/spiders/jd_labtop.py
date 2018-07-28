# -*- coding: utf-8 -*-
import scrapy


class JdLabtopSpider(scrapy.Spider):
    name = 'jd_labtop'
    allowed_domains = ['search.jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8']

    def parse(self, response):
        pass
