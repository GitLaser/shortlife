# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/2/21 20:45"

import pika

connect = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel =connect.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()