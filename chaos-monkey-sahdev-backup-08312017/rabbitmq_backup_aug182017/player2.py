#!/usr/bin/env python
import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('192.168.99.100', 32340, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.queue_declare(queue='table')

def callback(ch, method, properties, body):
    #print(" [x] Received ping %r" % body)
    print("Pong")

channel.basic_consume(callback,
                      queue='table',
                      no_ack=True)

print(' [*] Waiting for ping back. To exit press CTRL+C')
channel.start_consuming()
