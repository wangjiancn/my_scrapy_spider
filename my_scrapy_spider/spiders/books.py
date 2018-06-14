# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['book.toscrapy.com']
    start_urls = ['http://book.toscrapy.com/']

    def parse(self, response):
        pass
