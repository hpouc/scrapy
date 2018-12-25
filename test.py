# !/usr/bin/python
# coding:utf-8

import scrapy


class PublicSpider1(scrapy.Spider):
    """
    北极星电力新闻网(供电) 1500条 完成
    """
    name = 'public_utilities'

    start_urlss = ['http://news.bjx.com.cn/zt.asp?topic=%b9%a9%b5%e7%b9%ab%cb%be&page=1']
    a = [x for x in range(1, 30)]
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
                print(item)
                yield item
            # 本页其他新闻
            for next_url in response.xpath(next_url_xpath).extract():
                if next_url:
                    # print(next_url)
                    yield response.follow(next_url, callback=self.parse)

        except Exception as e:
            logger.error('error: %s' % e)