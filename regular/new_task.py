# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/2/21 22:32"

import pika
import sys

message = ' '.join(sys.argv[1:]) or 'hello world'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='new_taskque',durable=True)
channel.basic_publish(exchange='',
                      routing_key='new_task',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      )
                      )

channel.close()
