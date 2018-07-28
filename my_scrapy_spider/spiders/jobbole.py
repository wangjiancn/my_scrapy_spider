# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import JobbleItem


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    db_name = 'jobbolelist'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        next_page = LinkExtractor(restrict_css='.next.page-numbers')
        page_links = next_page.extract_links(response)
        if page_links:
            page_link = page_links[0].url
            yield scrapy.Request(page_link, callback=self.parse)
        article = LinkExtractor(restrict_css='a.archive-title')
        article_links = article.extract_links(response)
        if article_links:
            for article_link in article_links:
                yield scrapy.Request(article_link.url, callback=self.parse_page)

    def parse_page(self, response):
        jobbole_article = JobbleItem()
        jobbole_article['title'] = response.xpath("//div[@class='entry-header']/h1/text()").extract_first()
        jobbole_article['date'] = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").re_first(
            r'\d{4}/\d{1,2}/\d{1,2}')
        jobbole_article['praise'] = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").re_first('\d',
                                                                                                                  default=0)
        jobbole_article['fav'] = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").re_first('\d',
                                                                                                           default=0)
        jobbole_article['comments'] = response.xpath("//span[contains(@class,'btn-bluet-bigger')]/text()").re_first(
            '\d', default=0)
        jobbole_article['tag'] = list(
            set([member for member in response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract() if
                 not member.rstrip().endswith('评论')]))
        jobbole_article['web_address'] = response.url
        yield jobbole_article
        # author = response.xpath("//span[contains(@class,'btn-bluet-bigger')]/text()").re_first('\d')
