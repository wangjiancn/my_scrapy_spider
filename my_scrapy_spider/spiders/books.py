# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['http://books.toscrape.com/*']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        books = BookItem()

        for sel in response.css('article.product_pod'):
            books['name'] = sel.xpath('./h3/a/@title').extract_first()
            books['price'] = sel.css('p.price_color::text').extract_first()
            yield books
        # le = LinkExtractor(restrict_css= 'ul.pager li.next')
        # links = le.extract_links(response)
        # if links:
        #     next_url = links[0].url
        #     yield scrapy.Request(next_url,callback=self.parse)
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)
