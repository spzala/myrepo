#!/usr/bin/env python
import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters( host='localhost'))

credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('my-release-rabbitmq.default.svc.cluster.local', 32340, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='pingqueue')

channel.basic_publish(exchange='',
                      routing_key='pingqueue',
                      body='Throw the ball!')
print(" [x] Sent 'Threw the ball!'")
#connection.close()
