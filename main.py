import argparse

from scrapy.cmdline import execute

# parser = argparse.ArgumentParser(description='start scrapy spider')
# parser.add_argument('spider', type=str, help='name of spider')
# args = parser.parse_args()
# spider_name = args.spider
spider_name = 'energy'

try:
    execute(['scrapy', 'crawl', spider_name])
    # execute(['scrapy', 'crawl', spider_name, '-s', 'JOBDIR=./jobs/eastmoney'])
except KeyboardInterrupt:
    print('shut down by keyboard')
