#!/usr/bin/python
# coding:utf-8

import scrapy

""""
供电供热
"""


class PublicSpider01(scrapy.Spider):
    """北极星电力新闻网（供热、供电公司）"""
    name = 'public_utilities'
    start_urls = ['http://news.bjx.com.cn/html/20181217/949752.shtml']

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '//div[@class="list_detail"]/h1/text()'
        date_xpath = '//div[@class="list_copy"]/b[2]/text()'
        source_xpath = '//div[@class="list_copy"]/b[1]/text()'
        author_xpath = '//div[@class="list_copy"]/a[1]/text()'
        content_xpath = '//div[@id="content"]/p//text()'

        next_url_xpath = '//ul[@class="list_left_ul"]/li/a/@href'
        next_page_xpath = '//div[@class="pages"]/a[text()>= 2 and text()<=4]/@href'  #  限制抓取页数

        try:
            title = response.xpath(title_xpath).extract()
            date = response.xpath(date_xpath).extract_first()
            source = response.xpath(source_xpath).extract()
            author = response.xpath(author_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content)

            print(title)
            print(date)
            print(source)
            print(author)
            print(contents)
            # 本页其他新闻
            # for next_url in response.xpath(next_url_xpath).extract():
            #     if next_url:
            #         # print(next_url)
            #         yield response.follow(next_url, callback=self.parse)
            # # 翻页，递归抓取
            # next_page_urls = response.xpath(next_page_xpath).extract()
            # for next_page_url in next_page_urls:
            #     if next_page_url:
            #         yield scrapy.Request(next_page_url, callback=self.parse)

        except:
            print('ERROR!')


""""
燃气供应
"""


"""
水务供应
"""

