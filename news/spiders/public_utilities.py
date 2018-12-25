#!/usr/bin/python
# coding:utf-8

import logging
import scrapy
from news.items import NewsItem
import time
logger = logging.getLogger(__name__)

""""
供电供热
"""


# class PublicSpider2(scrapy.Spider):
#     """供热信息网"""
#     name = 'public_utilities'
#     start_urlss = ['http://www.china-heating.com/news/?list_11_2.html']
#     a = [x for x in range(2, 110)]
#     start_urls = []
#     for i in range(len(a)):
#         start_urls.append(start_urlss[0].replace('2', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="a"]/h1/text()'
#         content_xpath = '//div[@id="newsContent"]//text()'
#
#         next_url_xpath = '//*[@id="newsList"]/div[1]/dl/dd/ul/li/div/h4/a/@href'
#         next_page_xpath = '//div[@class="navBtn"]/a[text()>= 2 and text()<=7]/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '公用事业'
#                 item['small_class'] = '供电供热'
#                 item['title'] = title
#                 item['date'] = '2018-12-21 16:04:26'
#                 item['source'] = '供热信息网'
#                 item['author'] = '无'
#                 item['contents'] = contents
#                 # print(item)
#                 yield item
#             # 本页其他新闻
#             for next_url in response.xpath(next_url_xpath).extract():
#                 if next_url:
#                     print(next_url)
#                     yield response.follow(next_url, callback=self.parse)
#             # # 翻页，递归抓取
#             # next_page_urls = response.xpath(next_page_xpath).extract()
#             # for next_page_url in next_page_urls:
#             #     if next_page_url:
#             #         next_page = response.urljoin(next_page_url)
#             #         # print(next_page)
#             #         yield scrapy.Request(next_page, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)

class PublicSpider1(scrapy.Spider):
    """
    北极星电力新闻网(供电) 1500条 完成
    """
    name = 'public_utilities'

    start_urlss = ['http://news.bjx.com.cn/zt.asp?topic=%b9%a9%b5%e7%b9%ab%cb%be&page=1']
    a = [x for x in range(30, 45)]
    start_urls = []
    for i in range(len(a)):
        start_urls.append(start_urlss[0].replace('1', str(a[i])))

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '//div[8]/div[1]/div[1]/h1/text()'
        date_xpath = '//div[8]/div[1]/div[1]/div[1]/b[2]/text()'
        content_xpath = '//*[@id="content"]/p/text()'

        next_url_xpath = '//div[8]/div[1]/ul/li/a/@href'

        try:
            title = response.xpath(title_xpath).extract_first()
            date = response.xpath(date_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content)

            item = NewsItem()
            if title and content:
                item['large_class'] = '公用事业'
                item['small_class'] = '供电供热'
                item['title'] = title
                item['date'] = date
                item['source'] = '北极星电力新闻网'
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


""""燃气供应"""


# class PublicSpider3(scrapy.Spider):
#     """中国燃气网  3000条"""
#     name = 'public_utilities'
#     start_urlss = ['http://www.chinagas.org.cn/hangye/zixun/china/index_2.html']
#     a = [x for x in range(2, 130)]
#     start_urls = []
#     for i in range(len(a)):
#         start_urls.append(start_urlss[0].replace('2', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[4]/div[1]/div/h1/text()'
#         date_xpath = '//div[4]/div[1]/div/div[1]/text()[1]'
#         content_xpath = '//div[4]/div[1]/div/div[2]/p/text()'
#
#         next_url_xpath = '//div[3]/div[2]/div/div[4]/ul/li/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '公用事业'
#                 item['small_class'] = '燃气供应'
#                 item['title'] = title
#                 item['date'] = date.replace('日期：', '')
#                 item['source'] = '中国燃气网'
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


"""水务供应"""


# class PublicSpider4(scrapy.Spider):
#     """中国水网  3000条"""
#     name = 'public_utilities'
#     start_urlss = ['http://www.h2o-china.com/news/field?fid=3&page=1']
#     a = [x for x in range(1, 300)]
#     start_urls = []
#     for i in range(len(a)):
#         start_urls.append(start_urlss[0].replace('1', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[1]/div[1]//div[@class="newscontent_press"]/h1/text()'
#         date_xpath = '//div[1]/div[1]//div[@class="mt25 newscontent_press_con"]/p[1]/text()'
#         content_xpath = '//*[@id="txtedit"]/p//text()'
#
#         next_url_xpath = '//div[1]/div[1]/div[1]/ul/li/h3/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '公用事业'
#                 item['small_class'] = '水务供应'
#                 item['title'] = title
#                 item['date'] = date.replace('时间：', '')
#                 item['source'] = '中国水网'
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

