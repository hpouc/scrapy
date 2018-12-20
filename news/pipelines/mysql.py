# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from collections import defaultdict

import yaml

from utils.mysql_ctrl import MysqlCtrl

logger = logging.getLogger(__name__)


class NewsMysqlPipeline(object):

    def __init__(self, settings):
        self.store_queue_len = settings['STORE_QUEUE_LEN']
        self.config_file_path = settings['CONFIG_FILE_PATH']
        self.db_config_name = settings['DB_CONFIG_NAME']
        self.data_queue = defaultdict(list)
        self.insert_sql = {}
        self.db = None

    def process_item(self, item, spider):
        item_name, params = item.get_params()

        if item_name not in self.insert_sql:
            insert_sql = item.get_insert_sql()
            self.insert_sql[item_name] = insert_sql

        self.data_queue[item_name].append(params)

        if len(self.data_queue[item_name]) >= self.store_queue_len:
            ret = self.db.TB_insert(
                self.insert_sql[item_name], self.data_queue[item_name])
            if not ret:
                logger.error('insert data error !!!')
            else:
                logger.info('successfully insert %d items' %
                            len(self.data_queue[item_name]))

            self.data_queue[item_name] = []

    def open_spider(self, spider):

        with open(self.config_file_path) as f:
            config_info = yaml.load(f.read())

        db_info = config_info[self.db_config_name]

        self.db = MysqlCtrl(db_info)
        ret = self.db.connect()
        if not ret:
            logger.error('connect database error !')

    def close_spider(self, spider):

        for item_name, data_list in self.data_queue.items():

            if len(data_list) > 0:
                ret = self.db.TB_insert(self.insert_sql[item_name], data_list)
                if not ret:
                    logger.error('insert data error !!!')
                else:
                    logger.info('successfully insert %d items' %
                                len(self.data_queue[item_name]))

        self.db.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
