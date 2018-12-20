#!/usr/bin/python
# coding:utf-8
import logging
import scrapy
from news.items import NewsItem
logger = logging.getLogger(__name__)
"""
煤炭
"""


class EnergySpider6(scrapy.Spider):
    """国际石油网 国内要闻、国际要闻"""
    name = 'energy'
    start_urls = ['http://oil.in-en.com/news/intl/',
                  'http://oil.in-en.com/news/china/',
                  'http://oil.in-en.com/news/state/',
                  'http://oil.in-en.com/news/focus/',
                  'http://oil.in-en.com/news/view/']

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '//div[@class="c_content"]/h1/text()'
        date_xpath = '//div[@class="c_copy"]/b[2]/text()'
        source_xpath = '//div[@class="c_copy"]/b[1]/text()'
        author_xpath = '//div[@class="c_copy"]/a/text()'
        content_xpath = '//div[@class="content"]//text()'

        next_url_xpath = '//div[@class="clist sborder"]/ul/li/a/@href'
        next_page_xpath = '//div[@class="pages"]/a[text()>= 2 and text()<=4]/@href'  # 限制抓取页数

        item = NewsItem()
        try:
            large_class = '能源'
            small_class = '石油'
            title = response.xpath(title_xpath).extract_first()
            date = response.xpath(date_xpath).extract_first()
            source = response.xpath(source_xpath).extract_first()
            author = response.xpath(author_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content)

            item['large_class'] = large_class
            item['small_class'] = small_class
            item['title'] = title
            item['date'] = date
            item['source'] = source
            item['author'] = author
            item['contents'] = contents
            yield item

            # 本页其他新闻
            for next_url in response.xpath(next_url_xpath).extract():
                if next_url:
                    # print(next_url)
                    yield response.follow(next_url, callback=self.parse)
            # 翻页，递归抓取
            next_page_urls = response.xpath(next_page_xpath).extract()
            for next_page_url in next_page_urls:
                if next_page_url:
                    yield scrapy.Request(next_page_url, callback=self.parse)

        except Exception as e:
            logger.error('error: %s' % e)


# class EnergySpider1(scrapy.Spider):
#     """中国能源网"""
#     name = 'energy'
#     start_urls = ['http://www.cnenergynews.cn/mt/']
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="xltitle"]/text()'
#         date_xpath = '//span[@class="xltimerl"]/text()'
#         source_xpath = '//span[@class="laiyuan"]/span/text()'
#         author_xpath = '//span[@class="xlzrbjt"]/span/text()'
#         content_xpath = '//div[@class="TRS_Editor"]//p//text()'
#
#         next_url_xpath = '//div[@class="main4_left_m1_t"]/a/@href'
#         item = NewsItem()
#         try:
#             large_class = '能源'
#             small_class = '煤炭'
#             title = response.xpath(title_xpath).extract_first()
#             date = response.xpath(date_xpath).extract_first()
#             source = response.xpath(source_xpath).extract_first()
#             author = response.xpath(author_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#
#             contents = '\n'.join(content)
#             item['large_class'] = large_class
#             item['small_class'] = small_class
#             item['title'] = title
#             item['date'] = date
#             item['source'] = source
#             item['author'] = author
#             item['contents'] = contents
#             yield item
#
#             for next_url in response.xpath(next_url_xpath).extract():
#                 if next_url:
#                     yield response.follow(next_url, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)

#
# class EnergySpider2(scrapy.Spider):
#     """中国煤炭资源网"""
#     name = 'energy'
#     start_urls = ['http://www.sxcoal.com/news/index']  # 中国煤炭资源网
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="news-detail"]/h2/text()'
#         date_xpath = '//div[@class="info"]/span[3]/text()'
#         source_xpath = '//div[@class="info"]/span[1]/text()'
#         author_xpath = '//div[@class="content"]/p[@style=" line-height: 40px;"]/span/text()'
#         content_xpath = '//div[@class="content"]//p[@style="text-indent:2em;"]//text()'
#
#         next_url_xpath = '//div[@class="artnr"]/h4/a/@href'
#
#         try:
#             title = response.xpath(title_xpath).extract()
#             date = response.xpath(date_xpath).extract_first()
#             source = response.xpath(source_xpath).extract()
#             author = response.xpath(author_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#
#             contents = '\n'.join(content)
#             print(title, date, source, author, contents)
#
#             for next_url in response.xpath(next_url_xpath).extract():
#                 if next_url:
#                     yield response.follow(next_url, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)
#
#
# class EnergySpider3(scrapy.Spider):
#     """中国煤炭网"""
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
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="text-article"]/h1/text()'
#         date_xpath = '//div[@class="article-details"]/span[2]/text()'
#         source_xpath = '//div[@class="article-details"]/span[1]/text()'
#         author_xpath = '//div[@class="share-r fr"]/text()'
#         content_xpath = '//div[@class="content"]/p//text()'
#
#         next_url_xpath = '//div[@class="listPage-l fl"]/ul[1]//a/@href'
#         next_page_xpath = '//div[@class="listPage-l fl"]/ul[2]/following::li[@class="page page1"]/a/@hrf'
#
#         try:
#             title = response.xpath(title_xpath).extract()
#             date = response.xpath(date_xpath).extract_first()
#             source = response.xpath(source_xpath).extract()
#             author = response.xpath(author_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#
#             contents = '\n'.join(content)
#             print(title, date, source, author, contents)
#             next_urls = response.xpath(next_url_xpath).extract()
#             # 本页下一条新闻
#             for next_url in next_urls:
#                 if next_url:
#                     yield response.follow(next_url, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)
#
#
# """
# 石油及天然气
# """
#

# class EnergySpider6(scrapy.Spider):
#     """国际石油网 国内要闻、国际要闻"""
#     name = 'energy'
#     start_urls = ['http://oil.in-en.com/news/intl/',
#                   'http://oil.in-en.com/news/china/',
#                   'http://oil.in-en.com/news/state/',
#                   'http://oil.in-en.com/news/focus/',
#                   'http://oil.in-en.com/news/view/']
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="c_content"]/h1/text()'
#         date_xpath = '//div[@class="c_copy"]/b[2]/text()'
#         source_xpath = '//div[@class="c_copy"]/b[1]/text()'
#         author_xpath = '//div[@class="c_copy"]/a/text()'
#         content_xpath = '//div[@class="content"]//text()'
#
#         next_url_xpath = '//div[@class="clist sborder"]/ul/li/a/@href'
#         next_page_xpath = '//div[@class="pages"]/a[text()>= 2 and text()<=4]/@href'  # 限制抓取页数
#
#         item = NewsItem()
#         try:
#             large_class = '能源'
#             small_class = '石油'
#             title = response.xpath(title_xpath).extract()
#             date = response.xpath(date_xpath).extract_first()
#             source = response.xpath(source_xpath).extract()
#             author = response.xpath(author_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             item['large_class'] = large_class
#             item['small_class'] = small_class
#             item['title'] = title
#             item['date'] = date
#             item['source'] = source
#             item['author'] = author
#             item['contents'] = contents
#             yield item
#
#             # print(title)
#             # print(date)
#             # print(source)
#             # print(author)
#             # print(contents)
#             # 本页其他新闻
#             for next_url in response.xpath(next_url_xpath).extract():
#                 if next_url:
#                     # print(next_url)
#                     yield response.follow(next_url, callback=self.parse)
#             # 翻页，递归抓取
#             next_page_urls = response.xpath(next_page_xpath).extract()
#             for next_page_url in next_page_urls:
#                 if next_page_url:
#                     yield scrapy.Request(next_page_url, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)
#
#
# """
# 替代能源
# """
#
#
# class EnergySpider7(scrapy.Spider):
#     """北极星太阳能光伏网、北极星电力网、北极星核电网"""
#     name = 'energy'
#     start_urls = ['http://guangfu.bjx.com.cn/NewsList.aspx?page=1',
#                   'http://news.bjx.com.cn/list',
#                   'http://hedian.bjx.com.cn/NewsList']
#
#     def start_requests(self):
#         for start_url in self.start_urls:
#             yield scrapy.Request(start_url, callback=self.parse)
#
#     def parse(self, response):
#         title_xpath = '//div[@class="list_detail"]/h1/text()'
#         date_xpath = '//div[@class="list_copy"]/b[2]/text()'
#         source_xpath = '//div[@class="list_copy"]/b[1]/text()'
#         author_xpath = '//div[@class="list_copy"]/a[1]/text()'
#         content_xpath = '//div[@id="content"]/p//text()'
#
#         next_url_xpath = '//ul[@class="list_left_ul"]/li/a/@href'
#         next_page_xpath = '//div[@class="pages"]/a[text()>= 2 and text()<=4]/@href'  #  限制抓取页数
#
#         try:
#             title = response.xpath(title_xpath).extract()
#             date = response.xpath(date_xpath).extract_first()
#             source = response.xpath(source_xpath).extract()
#             author = response.xpath(author_xpath).extract_first()
#             content = response.xpath(content_xpath).extract()
#             contents = '\n'.join(content)
#
#             print(title)
#             print(date)
#             print(source)
#             print(author)
#             print(contents)
#             # 本页其他新闻
#             for next_url in response.xpath(next_url_xpath).extract():
#                 if next_url:
#                     # print(next_url)
#                     yield response.follow(next_url, callback=self.parse)
#             # 翻页，递归抓取
#             next_page_urls = response.xpath(next_page_xpath).extract()
#             for next_page_url in next_page_urls:
#                 if next_page_url:
#                     yield scrapy.Request(next_page_url, callback=self.parse)
#
#         except Exception as e:
#             logger.error('error: %s' % e)
#
#

