# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem


class booksspider(scrapy.Spider):
    name = 'books'
    db_name = 'bookslist'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        # books = bookitem()
        # for sel in response.css('article.product_pod'):
        #     books['name'] = sel.xpath('./h3/a/@title').extract_first()
        #     books['price'] = sel.css('p.price_color::text').extract_first()
        #     yield books
        # le = linkextractor(restrict_css='ul.pager li.next')
        # links = le.extract_links(response)
        # if links:
        #     next_url = links[0].url
        #     yield scrapy.request(next_url, callback=self.parse)
        page = LinkExtractor(restrict_css='ul.pager li.next')
        page_links = page.extract_links(response)
        if page_links:
            page_link = page_links[0].url
            yield scrapy.Request(page_link, callback=self.parse)
        le = LinkExtractor(restrict_css='article.product_pod h3')
        links = le.extract_links(response)
        if links:
            for next_url in links:
                yield scrapy.Request(next_url.url, callback=self.parse_book)

    def parse_book(self, response):
        books = BookItem()
        book = response.css('article.product_page')
        books['name'] = book.xpath('./div[1]/div[2]/h1/text()').extract_first()
        books['price'] = book.xpath('./div[1]/div[2]/p[1]/text()').extract_first()  # @后双引号
        books['stock'] = book.xpath('./div[1]/div[2]/p[2]/text()').re_first('\((\d+) available\)')
        books['review_rating'] = book.xpath('./div[1]/div[2]/p/@class').re_first('One|Two|Three|Four|Five')
        books['review_num'] = book.xpath('.//tr[7]/td/text()').extract_first()
        books['upc'] = book.xpath('.//tr[1]/td/text()').extract_first()
        yield books
