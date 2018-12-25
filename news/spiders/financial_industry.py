#!/usr/bin/python
# coding:utf-8

import logging
import scrapy
from news.items import NewsItem
import time
logger = logging.getLogger(__name__)
"""
金融业
"""

"""银行"""

class FinanceSpider3(scrapy.Spider):
    """
    中国经济网股票（大势研判、公司动态、并购重组、上市观察、行业新闻、板块研究、股指期货、海外市场）600*8条
    """
    name = 'financial_industry'

    start_urlss = ['http://finance.ce.cn/10cjsy/ds/index_1.shtml',
                   'http://finance.ce.cn/10cjsy/gs/index_1.shtml',
                   'http://finance.ce.cn/10cjsy/bg/index_1.shtml',
                   'http://finance.ce.cn/10cjsy/ss/index_1.shtml',
                   'http://finance.ce.cn/10cjsy/hy/index_1.shtml',
                   'http://finance.ce.cn/10cjsy/bk/index_1.shtml',
                   'http://finance.ce.cn/10cjsy/qt/index_1.shtml',
                   'http://finance.ce.cn/10cjsy/hw/index_1.shtml',
                   'http://finance.ce.cn/10cjsy/ds/index_1.shtml']

    a = [x for x in range(1, 4)]
    start_urls = []
    for j in range(8):
        for i in range(len(a)):
            start_urls.append(start_urlss[j].replace('_1', '_' + str(a[i])))

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '//*[@id="articleTitle"]/text()'
        date_xpath = '//*[@id="articleTime"]/text()'
        content_xpath = '//*[@id="articleText"]/div/p/text()'

        next_url_xpath = '//div[@class="content2"]/div[@class="list_left"]/table[@width="586"]//tr/td/a/@href'

        try:
            title = response.xpath(title_xpath).extract_first()
            date = response.xpath(date_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content)

            item = NewsItem()
            if title and content:
                item['large_class'] = '金融业'
                item['small_class'] = '证券'
                item['title'] = title.strip()
                item['date'] = date.replace('年', '-').replace('月', '-').replace('日', '').strip()  # 日期格式转换
                item['source'] = '中国经济网'
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

