#!/usr/bin/python
# coding:utf-8

import logging
import scrapy
from news.items import NewsItem
import time
logger = logging.getLogger(__name__)

"""
消费品制造业
"""

"""乳制品"""


#
# class FinanceSpider1(scrapy.Spider):
#     """
#     中国经济网 乳业 15000条
#     """
#     name = 'consumer_goods_manufacturing'
#
#     start_urlss = ['http://www.ce.cn/cysc/sp/ry/index_1.shtml']
#     a = [x for x in range(2)]
#     start_urls = ['http://www.ce.cn/cysc/sp/ry/']
#     for i in range(len(a)):
#         start_urls.append(start_urlss[0].replace('_2', '_' + str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//*[@id="articleTitle"]/text()'
#         date_xpath = '//*[@id="articleTime"]/text()'
#         content_xpath = '//*[@id="articleText"]/div/p/text()'
#
#         next_url_xpath = '//div[@class="left"]/ul/li/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content).strip()
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '消费品制造业'
#                 item['small_class'] = '乳制品'
#                 item['title'] = title.strip()
#                 item['date'] = date.replace('年', '-').replace('月', '-').replace('日', '').strip()  # 日期格式转换
#                 item['source'] = '中国经济网'
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


# """医疗器械"""
#
# class FinanceSpider3(scrapy.Spider):
#     """
#     医疗器械网 医疗器械 15000条
#     """
#     name = 'consumer_goods_manufacturing'
#
#     start_urlss = ['http://www.chinamedevice.cn/news_ylqx/news/index0.html',
#                    'http://www.chinamedevice.cn/news_cjxw/news/index0.html',
#                    ]
#     a = [x for x in range(0, 20)]
#     start_urls = []
#     for j in range(2):
#         for i in range(len(a)):
#             start_urls.append(start_urlss[j].replace('0', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//*[@id="left"]/div[1]/h1/text()'
#         # date_xpath = '//*[@id="articleTime"]/text()'
#         content_xpath = '//*[@id="remark_view"]/div/div//text()'
#
#         next_url_xpath = '/html/body/table[3]//tr/td[1]/table//tr/td/table//tr[1]/td/table//tr/td[2]/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             # date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content).strip()
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '消费品制造业'
#                 item['small_class'] = '医疗器械及服务'
#                 item['title'] = title.strip()
#                 item['date'] = '2018-12-25 15:17'  # 日期格式转换
#                 item['source'] = '医疗器械网'
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

# """进出口贸易"""
#
# class FinanceSpider3(scrapy.Spider):
#     """
#     进出口网 进出口贸易 15000条
#     """
#     name = 'consumer_goods_manufacturing'
#
#     start_urlss = ['http://www.chinainout.com/news/4693/2',
#                    ]
#     a = [x for x in range(2, 50)]
#     start_urls = ['http://www.chinainout.com/news/4693/']
#     for j in range(1):
#         for i in range(len(a)):
#             start_urls.append(start_urlss[j].replace('2', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="pos"]/h1/text()'
#         # date_xpath = '//*[@id="articleTime"]/text()'
#         content_xpath = '//div[@class="content"]//text()'
#
#         next_url_xpath = '//div[@class="catlist"]/ul/li/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             # date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content).strip()
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '消费品制造业'
#                 item['small_class'] = '进出口贸易'
#                 item['title'] = title.strip()
#                 item['date'] = '2018-12-25 15:17'  # 日期格式转换
#                 item['source'] = '进出口网'
#                 item['author'] = '无'
#                 item['contents'] = contents
#                 print(item)
#                 # yield item
#             # 本页其他新闻
#             for next_url in response.xpath(next_url_xpath).extract():
#                 if next_url:
#                     print(next_url)
#                     yield response.follow(next_url, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)


# """生物科技"""
#
# class FinanceSpider7(scrapy.Spider):
#     """
#     中国生物技术信息网  15000条
#     """
#     name = 'consumer_goods_manufacturing'
#
#     start_urlss = ['http://www.biotech.org.cn/news/page/1',
#                    ]
#     a = [x for x in range(1, 50)]
#     start_urls = []
#     for j in range(1):
#         for i in range(len(a)):
#             start_urls.append(start_urlss[j].replace('1', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@id="caption"]/text()'
#         date_xpath = '//div[@id="date"]/text()[3]'
#         content_xpath = '//div[@id="nr"]/p//text()'
#
#         next_url_xpath = '//div[@id="left"]/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content).strip()
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '消费品制造业'
#                 item['small_class'] = '生物科技'
#                 item['title'] = title.strip()
#                 item['date'] = date.replace('日期：', '')  # 日期格式转换
#                 item['source'] = '中国生物技术信息网'
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

"""美容及个人护理"""

class FinanceSpider7(scrapy.Spider):
    """
    聚美丽  15000条
    """
    name = 'consumer_goods_manufacturing'

    start_urlss = ['http://www.jumeili.cn/index-2-1.html',
                   ]
    a = [x for x in range(1, 60)]
    start_urls = []
    for j in range(1):
        for i in range(len(a)):
            start_urls.append(start_urlss[j].replace('1', str(a[i])))

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '//div[@class="hd meta"]/h1/text()'
        date_xpath = '//time[@class="time"]/text()'
        content_xpath = '//div[@id="Cnt-Main-Article-JML"]//p/text()'

        next_url_xpath = '//div[@class="item-content"]/a/@href'

        try:
            title = response.xpath(title_xpath).extract_first()
            date = response.xpath(date_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content).strip()

            item = NewsItem()
            if title and content:
                item['large_class'] = '消费品制造业'
                item['small_class'] = '美容及个人护理'
                item['title'] = title.strip()
                item['date'] = date.strip()  # 日期格式转换
                item['source'] = '聚美丽'
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