#!/usr/bin/python
# coding:utf-8
import logging
import scrapy
from news.items import NewsItem
import time
logger = logging.getLogger(__name__)
"""
煤炭
"""


# class EnergySpider1(scrapy.Spider):
#     """国际煤炭网 1600条"""
#     name = 'energy'
#     start_urlss = ['http://coal.in-en.com/news/intl/list41-2.html']
#     a = [x for x in range(75, 100)]
#     start_urls = []
#     for i in range(len(a)):
#         start_urls.append(start_urlss[0].replace('2', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="c_content"]/h1/text()'
#         date_xpath = '//div[@class="c_copy"]/b[2]/text()'
#         content_xpath = '//div[@class="content"]//text()'
#
#         next_url_xpath = '//div[@class="clist sborder"]/ul//a/@href'
#         next_page_xpath = '//div[@class="pages"]/a[text()>= 2 and text()<= 7]'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '能源'
#                 item['small_class'] = '煤炭'
#                 item['title'] = title
#                 item['date'] = date.replace('日期：', '')
#                 item['source'] = '国际煤炭网'
#                 item['author'] = '无'
#                 item['contents'] = contents
#
#                 # print(item)
#                 yield item
#
#             for next_url in response.xpath(next_url_xpath).extract():
#                 if next_url:
#                     yield response.follow(next_url, callback=self.parse)
#             # # 翻页，递归抓取
#             # next_page_urls = response.xpath(next_page_xpath).extract()
#             # for next_page_url in next_page_urls:
#             #     if next_page_url:
#             #         yield scrapy.Request(next_page_url, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)


#
# class EnergySpider3(scrapy.Spider):
#     """中国煤炭网  200条"""
#     name = 'energy'
#     start_urls = ['http://www.ccoalnews.com/news/yaowen.html',
#                   'http://www.ccoalnews.com/news/yaowen_2.html',
#                   'http://www.ccoalnews.com/news/yaowen_3.html',
#                   'http://www.ccoalnews.com/news/yaowen_4.html',
#                   'http://www.ccoalnews.com/news/yaowen_5.html',
#                   'http://www.ccoalnews.com/news/yaowen_6.html',
#                   'http://www.ccoalnews.com/news/yaowen_7.html',
#                   'http://www.ccoalnews.com/news/yaowen_8.html',
#                   'http://www.ccoalnews.com/news/yaowen_9.html',
#                   'http://www.ccoalnews.com/news/yaowen_10.html',]  # 中国煤炭网
#     # start_urls = ['http://www.ccoalnews.com/news/yaowen_2.html',]
#
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="text-article"]/h1/text()'
#         date_xpath = '//div[@class="article-details"]/span[2]/text()'
#         content_xpath = '//div[@class="content"]/p//text()'
#
#         next_url_xpath = '//div[@class="listPage-l fl"]/ul[1]//a/@href'
#         next_page_xpath = '//div[@class="listPage-l fl"]/ul[2]/following::li[@class="page page1"]/a/@hrf'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '能源'
#                 item['small_class'] = '煤炭'
#                 item['title'] = title
#                 if len(date) == 19:
#                     item['date'] = date
#                 else:
#                      item['date'] = '2018-12-18 09:44:56'
#                 item['source'] = '中国煤炭网'
#                 item['author'] = '无'
#                 item['contents'] = contents
#
#                 # print(item)
#                 yield item
#
#             next_urls = response.xpath(next_url_xpath).extract()
#             # 本页下一条新闻
#             for next_url in next_urls:
#                 if next_url:
#                     # print(next_url)
#                     yield response.follow(next_url, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)


#
# """
# 石油及天然气
# """
#
#
class EnergySpider6(scrapy.Spider):
    """国际石油网 国内要闻、国际要闻  3000条"""
    name = 'energy'
    start_urlss = [
                   'http://oil.in-en.com/news/intl/list128-2.html',
                   'http://oil.in-en.com/news/focus/list269-2.html',
                   ]
    a = [x for x in range(44, 110)]
    start_urls = []
    for j in range(0, 2):
        for i in range(len(a)):
            start_urls.append(start_urlss[j].replace('2', str(a[i])))

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '//div[@class="c_content"]/h1/text()'
        date_xpath = '//div[@class="c_copy"]/b[2]/text()'
        content_xpath = '//div[@class="content"]//text()'

        next_url_xpath = '//div[@class="clist sborder"]/ul/li/a/@href'
        # next_page_xpath = '//div[@class="pages"]/a[text()>= 2 and text()<=4]/@href'  # 限制抓取页数

        item = NewsItem()
        try:
            title = response.xpath(title_xpath).extract_first()
            date = response.xpath(date_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content).strip()

            item = NewsItem()
            if title and content:

                item['large_class'] = '能源'
                item['small_class'] = '石油'
                item['title'] = title
                item['date'] = date.replace('日期：', '')
                item['source'] = '国际石油网'
                item['author'] = '无'
                item['contents'] = contents

                print(item)
                # yield item

            # 本页其他新闻
            for next_url in response.xpath(next_url_xpath).extract():
                if next_url:
                    # print(next_url)
                    yield response.follow(next_url, callback=self.parse)
            # # 翻页，递归抓取
            # next_page_urls = response.xpath(next_page_xpath).extract()
            # for next_page_url in next_page_urls:
            #     if next_page_url:
            #         yield scrapy.Request(next_page_url, callback=self.parse)

        except Exception as e:
            logger.error('error: %s' % e)


"""
替代能源
"""

#
# class EnergySpider7(scrapy.Spider):
#     """北极星太阳能光伏网 1000条 完成
#     北极星电力网 1000条
#     北极星核电网 1000条
#
#     """
#     name = 'energy'
#     start_urls = ['http://guangfu.bjx.com.cn/NewsList.aspx?page=21',
#                   'http://news.bjx.com.cn/list?page=21',
#                   'http://hedian.bjx.com.cn/NewsList?page=21']
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="list_detail"]/h1/text()'
#         date_xpath = '//div[@class="list_copy"]/b[2]/text()'
#         content_xpath = '//div[@id="content"]/p//text()'
#
#         next_url_xpath = '//ul[@class="list_left_ul"]/li/a/@href'
#         next_page_xpath = '//div[@class="page"]/a[text()>= 22 and text()<=30]/@href'  # 限制抓取页数
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '能源'
#                 item['small_class'] = '替代能源'
#                 item['title'] = title
#                 item['date'] = date
#                 item['source'] = '北极星电力网'
#                 item['author'] = '无'
#                 item['contents'] = contents
#
#                 yield item
#             # 本页其他新闻
#             for next_url in response.xpath(next_url_xpath).extract():
#                 if next_url:
#                     # print(next_url)
#                     yield response.follow(next_url, callback=self.parse)
#             # 翻页，递归抓取
#             next_page_urls = response.xpath(next_page_xpath).extract()
#             for next_page_url in next_page_urls:
#                 if next_page_url:
#                     next_page = response.urljoin(next_page_url)
#                     # print(next_page)
#                     yield scrapy.Request(next_page, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)



