# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy import Item
import MySQLdb


class MongoDBPipeline:
    def open_spider(self, spider):
        # db_uri = spider.settings.get('MONGODB_URI', 'mongodb://localhost:27017')
        # db_name = spider.settings.get('MONGODB_DB_NAME', 'scrapy_default')
        #
        # self.db_client = MongoClient('mongodb://localhost:27017')
        # self.db = self.db_client[db_name]
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['books']
        self.collection = self.db[spider.db_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        if isinstance(item, Item):
            item = dict(item)

        self.collection.insert_one(item)


class MySQLPipeline:
    def open_spider(self, spider):
        self.client = MySQLdb.connect(host='localhost',
                                      user='python2',
                                      passwd='python2',
                                      port=3306,
                                      db='books')
        self.cursor = self.client.cursor()

    def close_spider(self, spider):
        self.client.commit()
        self.client.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (item['name'], item['price'])
        sql = 'insert into books values(%s,%s)'
        self.cursor.execute(sql, values)
# class MyScrapySpiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
