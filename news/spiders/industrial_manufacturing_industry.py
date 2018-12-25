#!/usr/bin/python
# coding:utf-8

import logging
import scrapy
from news.items import NewsItem
import time
logger = logging.getLogger(__name__)

"""
工业制造品业
"""

# """船舶制造"""
#
# class FinanceSpider7(scrapy.Spider):
#     """
#     船舶设备网  15000条
#     """
#     name = 'industrial_manufacturing_industry'
#
#     start_urlss = ['http://www.cbsbw.com/news/list-877-2.html',
#                    ]
#     a = [x for x in range(30, 45)]
#     start_urls = ['http://www.cbsbw.com/news/list-877.html']
#     for j in range(1):
#         for i in range(len(a)):
#             start_urls.append(start_urlss[j].replace('-2', '-'+str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="shownewscontent"]/h2/text()'
#         date_xpath = '//div[@class="news_desc"]/span/text()'
#         content_xpath = '//div[@class="shownewscontent"]//p/text()'
#
#         next_url_xpath = '//div[@class="bgnews"]/h2/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content).strip()
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '工业制造品'
#                 item['small_class'] = '船舶制造'
#                 item['title'] = title.strip()
#                 item['date'] = date.replace('发布日期：', '').strip()  # 日期格式转换
#                 item['source'] = '船舶设备网'
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

"""环保"""

# class FinanceSpider7(scrapy.Spider):
#     """
#     船舶设备网  15000条
#     """
#     name = 'industrial_manufacturing_industry'
#
#     start_urlss = ['http://www.hbzhan.com/news/t14/list_p2.html',
#                    ]
#     a = [x for x in range(25, 90)]
#     start_urls = []
#     for j in range(1):
#         for i in range(len(a)):
#             start_urls.append(start_urlss[j].replace('2', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="leftTop"]/text()'
#         date_xpath = '//div[@class="leftTop"]/p[1]/span[1]/text()'
#         content_xpath = '//div[@class="newsContent"]/div//text()'
#
#         next_url_xpath = '//div[@class="listLeft"]/div[@class="leftBox"]/h3/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content).strip()
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '工业制造品'
#                 item['small_class'] = '环保'
#                 item['title'] = title.strip()
#                 item['date'] = date.strip()  # 日期格式转换
#                 item['source'] = '中国环保在线'
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

"""机械装备及器材"""

class FinanceSpider7(scrapy.Spider):
    """
    船舶设备网  15000条
    """
    name = 'industrial_manufacturing_industry'

    start_urlss = ['http://info.machine.hc360.com/list/list_gndt_1-2.shtml',
                   ]
    a = [x for x in range(2, 11)]
    start_urls = ['http://info.machine.hc360.com/list/list_gndt_1.shtml']
    for j in range(1):
        for i in range(len(a)):
            start_urls.append(start_urlss[j].replace('-2', '-'+str(a[i])))

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '//div[@id="title"]/h1/text()'
        date_xpath = '//div[@class="wzzzly"]/span[2]/text()'
        content_xpath = '//div[@id="artical"]/p//text()'

        next_url_xpath = '//div[@class="news_list"]//tr/td/a/@href'

        try:
            title = response.xpath(title_xpath).extract_first()
            date = response.xpath(date_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content).strip()

            item = NewsItem()
            if title and content:
                item['large_class'] = '工业制造品'
                item['small_class'] = '机械装备及器材'
                item['title'] = title.strip()
                item['date'] = date.replace('年', '-').replace('月', '-').replace('日', ' ').strip()  # 日期格式转换
                item['source'] = '慧聪机械工业网'
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