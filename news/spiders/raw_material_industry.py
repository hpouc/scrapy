#!/usr/bin/python
# coding:utf-8

import logging
import scrapy
from news.items import NewsItem
import time
logger = logging.getLogger(__name__)
"""
原材料业
"""

"""化工产品"""



"""橡胶"""


# class RawSpider3(scrapy.Spider):
#     """中国橡胶网 """
#     name = 'raw_material_industry'
#
#     start_urlss = ['http://www.cria.org.cn/newslist/6.html?p=2',
#                    'http://www.cria.org.cn/newslist/3.html?p=2']
#     a = [x for x in range(2, 40)]
#     start_urls = []
#     for j in range(2):
#         for i in range(len(a)):
#             start_urls.append(start_urlss[j].replace('2', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="enterprise_news_t"]/h1/text()'
#         date_xpath = '//div[@class="enterprise_news02 p30"]/div[@class="enterprise_news_t"]/span[1]/text()'
#         content_xpath = '//div[@class="news_details_c p20"]/p/span/text()'
#
#         next_url_xpath = '//div[5]/div/div[1]/div/div[1]/ul/li/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '原材料业'
#                 item['small_class'] = '橡胶'
#                 item['title'] = title
#                 item['date'] = date.replace('发布时间：', '')
#                 item['source'] = '中国橡胶网'
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


# """钢铁"""
#
#
# class RawSpider4(scrapy.Spider):
#     """钢易网 """
#     name = 'raw_material_industry'
#
#     start_urlss = ['http://www.gtgqw.com/second/hysj1.html']
#     a = [x for x in range(70, 140)]
#     start_urls = []
#
#     for i in range(len(a)):
#         start_urls.append(start_urlss[0].replace('1', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="title"]/h1/text()'
#         date_xpath = '//div[@class="changgui"]/text()'
#         content_xpath = '//div[@class="content"]/p//text()'
#
#         next_url_xpath = '//div[@class="main"]//ul//p/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '原材料业'
#                 item['small_class'] = '钢铁'
#                 item['title'] = title
#                 item['date'] = date.replace('http://www.gtgqw.com 钢易网 ', '')
#                 item['source'] = '钢易网'
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

"""造纸"""


# class RawSpider5(scrapy.Spider):
#     """中国行业经济 纸品 """
#     name = 'raw_material_industry'
#
#     start_urlss = ['http://www.sizo.com.cn/paper/2.html']
#     a = [x for x in range(2, 40)]
#     start_urls = []
#
#     for i in range(len(a)):
#         start_urls.append(start_urlss[0].replace('2', str(a[i])))
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//*[@id="view_article"]//tr[2]/td/div[1]/span/font/text()'
#         date_xpath = '//*[@id="view_article"]//tr[2]/td/span/div[1]/a[1]/span/text()'
#         content_xpath = '//*[@id="post1"]/p/span/text()'
#
#         next_url_xpath = '//*[@id="list_article"]//tr[2]/td/table//tr/td/span[1]/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content).strip()
#
#             item = NewsItem()
#             if title and content:
#                 item['large_class'] = '原材料业'
#                 item['small_class'] = '造纸'
#                 item['title'] = title
#                 item['date'] = date
#                 item['source'] = '中国行业经济网'
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

class RawSpider6(scrapy.Spider):
    """中国纸网 国内 """
    name = 'raw_material_industry'

    start_urls = ['http://www.paper.com.cn/news/nation.php?news_type=%B2%C6%BE%AD%D0%C2%CE%C5&page=1']
    # a = [x for x in range(2, 40)]
    # start_urls = []
    #
    # for i in range(len(a)):
    #     start_urls.append(start_urlss[0].replace('2', str(a[i])))

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '/html/body/div[2]/table[4]//tr/td[1]/table[1]//tr/td/table[1]//tr[1]/td/div/b/text()'
        date_xpath = '/html/body/div[2]/table[4]//tr/td[1]/table[1]//tr/td/table[2]//tr[2]/td/div/font/span/text()'
        content_xpath = '/html/body/div[2]/table[4]//tr/td[1]/table[1]//tr/td/table[3]//tr[1]/td/p/text()'

        next_url_xpath = '/html/body/table[1]//tr[2]/td/table//tr/td[1]/table//tr[2]/td/table[1]//tr/td[2]/a/@href'

        try:
            title = response.xpath(title_xpath).extract_first()
            date = response.xpath(date_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content).strip()

            item = NewsItem()
            if title and content:
                item['large_class'] = '原材料业'
                item['small_class'] = '造纸'
                item['title'] = title
                item['date'] = date
                item['source'] = '中国纸网'
                item['author'] = '无'
                item['contents'] = contents
                print(item)
                # yield item
            # 本页其他新闻
            for next_url in response.xpath(next_url_xpath).extract():
                if next_url:
                    print(next_url)
                    yield response.follow(next_url, callback=self.parse)

        except Exception as e:
            logger.error('error: %s' % e)