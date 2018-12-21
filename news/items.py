# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from utils.md5 import md5


class NewsItem(scrapy.Item):
    large_class = scrapy.Field()
    small_class = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    author = scrapy.Field()
    contents = scrapy.Field()

    item_name = 'news'

    def get_params(self):
        large_class = self.get('large_class')
        small_class = self.get('small_class')
        title = self.get('title')
        date = self.get('date')
        source = self.get('source')
        author = self.get('author')
        contents = self.get('contents')

        derepeat_md5 = md5(title + '@' + source)
        title_md5 = md5(title)
        params = (large_class, small_class, title, date, source, author, contents, derepeat_md5, title_md5)

        return self.item_name, params

    def get_insert_sql(self):
        insert_sql = 'INSERT IGNORE INTO test' \
                     '(large_class, small_class, title, date, source, author, contents, derepeat_md5, title_md5) ' \
                     'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'

        return insert_sql

