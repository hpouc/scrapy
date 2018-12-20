#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from logging.config import dictConfig
import sys


class logger(object):

    @classmethod
    def init(cls, log_filename, log_name):
        logging_config = {
            'version': 1,
            'formatters': {
                'f1': {
                    'format': '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S',
                }
            },

            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'f1',
                    'level': 'INFO'
                },

                'file': {
                    'class': 'logging.handlers.TimedRotatingFileHandler',
                    'formatter': 'f1',
                    'level': 'INFO',
                    'filename': log_filename,
                    'when': 'midnight',
                    'backupCount': 3,
                }
            },    

            'root': {
                    'handlers': ['console', 'file'],
                    'level': 'WARN'
                },
            
            'loggers': {
                'mylogger': {
                    'handlers': ['console', 'file'],
                    'level': 'INFO',
                    "propagate": False
                }
            }
        }

        dictConfig(logging_config)

        cls.log = logging.getLogger(log_name)
