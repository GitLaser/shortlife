# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/12 11:33"

import re

ex="For this reason, you should set your <t0>SESSION_COOKIE_SECURE</t0> and <t3>CSRF_COOKIE_SECURE</t3> settings to <t6>True</t6>."
ex=ex.replace('原文： ','')
result = re.sub(r'<(/t|t)[\d]>','',ex,re.M|re.I)

print(result)

