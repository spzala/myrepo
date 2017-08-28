#!/usr/bin/env python
import pika
import sys
import time

credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('192.168.99.100', 32340, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='pingqueue')
channel.queue_declare(queue='pongqueue')

def callback(ch, method, properties, body):
    print(" [x] Plaer 1 Received ping %r" % body)
    print("Player 1 sending ping")
    time.sleep(2)
    channel.basic_publish(exchange='',
                  	routing_key='pingqueue',
                  	body="Ping")
channel.basic_consume(callback,
                      	queue='pongqueue',
                      	no_ack=True)
print(' [*] Waiting for ping back. To exit press CTRL+C')

channel.start_consuming()
