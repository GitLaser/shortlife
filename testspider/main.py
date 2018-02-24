# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/2/3 19:59"

import os
import sys


from scrapy.cmdline import execute


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','bole'])