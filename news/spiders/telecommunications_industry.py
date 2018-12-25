#!/usr/bin/python
# coding:utf-8

import scrapy

"""
电讯业
"""

class TeleSpider1(scrapy.Spider):
    """
    中国经济网（滚动新闻、行业新闻、要闻）2400条
    """
    name = 'telecommunications_industry'

    start_urlss = ['http://finance.ce.cn/bank12/scroll/index_1.shtml',
                   'http://finance.ce.cn/bank/sryh/index_1.shtml',
                   'http://finance.ce.cn/bank/yw/index_1.shtml']
    a = [x for x in range(1, 5)]
    start_urls = ['http://finance.ce.cn/bank12/scroll/index.shtml',
                  'http://finance.ce.cn/bank/sryh/',
                  'http://finance.ce.cn/bank/yw/index.shtml']
    for j in range(3):
        for i in range(len(a)):
            start_urls.append(start_urlss[j].replace('_1', '_' + str(a[i])))

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        title_xpath = '//*[@id="articleTitle"]/text()'
        date_xpath = '//*[@id="articleTime"]/text()'
        content_xpath = '//*[@id="articleText"]/div/p/text()'

        next_url_xpath = '//div[4]/div[1]/table[2]/tbody/tr/td/a/@href'

        try:
            title = response.xpath(title_xpath).extract_first()
            date = response.xpath(date_xpath).extract_first()
            content = response.xpath(content_xpath).extract()
            contents = '\n'.join(content)

            item = NewsItem()
            if title and content:
                item['large_class'] = '金融业'
                item['small_class'] = '银行'
                item['title'] = title
                item['date'] = date.replace('年', '-').replace('月', '-').replace('日', '-')  # 日期格式转换
                item['source'] = '中国经济网'
                item['author'] = '无'
                item['contents'] = contents
                # print(item)
                yield item
            # 本页其他新闻
            for next_url in response.xpath(next_url_xpath).extract():
                if next_url:
                    # print(next_url)
                    yield response.follow(next_url, callback=self.parse)

        except Exception as e:
            logger.error('error: %s' % e)