# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/2/21 22:35"

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='new_taskque',durable=True)
def callback(ch,method,properties,body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='new_task',
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()