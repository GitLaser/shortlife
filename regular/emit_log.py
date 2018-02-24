# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/2/23 21:57"

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange_type='fanout',exchange='logs')
message = 'Tutoral 3 -- Publish and Subscribe'
channel.basic_publish(exchange='logs',routing_key='',body=message)
print(__file__,'sent %r' % message)
channel.close()



