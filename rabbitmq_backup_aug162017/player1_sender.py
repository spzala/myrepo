#!/usr/bin/env python
import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters( host='localhost'))

credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('192.168.99.100', 32340, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.queue_declare(queue='table')

channel.basic_publish(exchange='',
                      routing_key='table',
                      body='Pong this ping!')
print(" [x] Sent 'Pong this ping!'")
connection.close()
