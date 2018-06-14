# -*- coding: utf-8 -*-
import scrapy
from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['http://books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        books = BookItem()

        for sel in response.css('article.product_pod'):
            # books['name'] = sel.xpath('./h3/a/@title').extract_first()
            # books['price'] = sel.css('p.price_color::text').extract_first()
            books['name'] = sel.xpath('./h3/a/@title').extract_first()
            books['price'] = sel.css('p.price_color::text').extract_first()
            # books['praise'] = product.
            yield books

    # def parse(self, response):
    #    for sel in response.css('article.product_pod'):
    #       name = sel.xpath('./h3/a/@title').extract_first()
    #       price= sel.css('p.price_color::text').extract_first()
    #       yield {
    #           'name':name,
    #           'price':price
    #       }
