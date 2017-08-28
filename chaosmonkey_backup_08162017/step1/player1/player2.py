#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('192.168.99.100', 32340, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='pingqueue')
channel.queue_declare(queue='pongqueue')

def callback(ch, method, properties, body):
    print(" Player2 received ping %r" % body)
    time.sleep(2)
    channel.basic_publish(exchange='',
                  routing_key='pongqueue',
                  body="Ping back")
    
channel.basic_consume(callback,
                      queue='pingqueue',
                      no_ack=True)

print(' Player2 is waiting for ping back. To exit press CTRL+C')
channel.start_consuming()
