# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/2/21 20:30"

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
# for i in range(20):
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='task 1')
    # print(" [x] Sent 'task %d!'" % i)
connection.close()

