#!/usr/bin/python
# coding:utf-8

import logging
import scrapy
from news.items import NewsItem
import time
logger = logging.getLogger(__name__)
"""
畜牧种植业
"""

"""种植业"""


# class LivestockSpider1(scrapy.Spider):
#     """中国农业新闻网 各1000条"""
#     name = 'livestock_farming'
#     start_urlss = [
#                    'http://www.farmer.com.cn/jjpd/zzy/xdzy/index_1.htm',
#                    'http://www.farmer.com.cn/jjpd/zzy/xdnysfq/index_1.htm',
#                    'http://www.farmer.com.cn/jjpd/zzy/nybzy/index_1.htm']
#     a = [x for x in range(1, 25)]
#     start_urls = []
#     for j in range(3):
#         for i in range(len(a)):
#             start_urls.append(start_urlss[j].replace('1', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[4]/div/div[1]/div/div/h1/text()'
#         date_xpath = '//div[4]/div/div[1]/div/div/div[1]/div/div[1]/p/text()[1]'
#         content_xpath = '//div[4]/div/div[1]/div/div/div[2]/div[1]/p/text()'
#
#         next_url_xpath = '//div[4]/div/div[1]/div/div/div[2]/div/div/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '畜牧养殖业'
#                 item['small_class'] = '种植业'
#                 item['title'] = title
#                 item['date'] = date
#                 item['source'] = '中国农业新闻网'
#                 item['author'] = '无'
#                 item['contents'] = contents
#                 # print(item)
#                 yield item
#             # 本页其他新闻
#             for next_url in response.xpath(next_url_xpath).extract():
#                 if next_url:
#                     print(next_url)
#                     yield response.follow(next_url, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)


"""养殖业"""


class LivestockSpider2(scrapy.Spider):
    """中国农业新闻网 每一类1000条"""
    name = 'livestock_farming'
    start_urlss = ['http://www.farmer.com.cn/jjpd/xm/xmdt/index_1.htm',
                   'http://www.farmer.com.cn/jjpd/xm/dsc/index_1.htm',
                   'http://www.farmer.com.cn/jjpd/xm/ql/index_1.htm',
                   'http://www.farmer.com.cn/jjpd/xm/slyfk/index_1.htm',
                   'http://www.farmer.com.cn/jjpd/xm/tzyz/index_1.htm',]
    a = [x for x in range(1, 25)]
    start_urls = []
    for j in range(5):
        for i in range(len(a)):
            start_urls.append(start_urlss[j].replace('1', str(a[i])))

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '//div[4]/div/div[1]/div/div/h1/text()'
        date_xpath = '//div[4]/div/div[1]/div/div/div[1]/div/div[1]/p/text()[1]'
        content_xpath = '//div[4]/div/div[1]/div/div/div[2]/div[1]/p/text()'

        next_url_xpath = '/html/body/div[4]/div/div[1]/div/div/div[2]/div/div/a/@href'

        try:
            title = response.xpath(title_xpath).extract_first()
            date = response.xpath(date_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content)

            item = NewsItem()
            if title and content:
                item['large_class'] = '畜牧养殖业'
                item['small_class'] = '畜牧养殖'
                item['title'] = title
                item['date'] = date
                item['source'] = '中国农业新闻网'
                item['author'] = '无'
                item['contents'] = contents
                # print(item)
                yield item
            # 本页其他新闻
            for next_url in response.xpath(next_url_xpath).extract():
                if next_url:
                    print(next_url)
                    yield response.follow(next_url, callback=self.parse)

        except Exception as e:
            logger.error('error: %s' % e)