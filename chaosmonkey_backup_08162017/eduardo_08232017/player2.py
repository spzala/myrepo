#!/usr/bin/env python
import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('192.168.99.100', 32340, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.queue_declare(queue='pingqueue')
channel.queue_declare(queue='pongqueue')

def callback(ch, method, properties, body):
    #print(" [x] Received ping %r" % body)
    print("Pong")
    channel.basic_publish(exchange='',
                  routing_key='pongqueue',
                  body="Ping back")
    print("Sent ping back on pongqueue")

channel.basic_consume(callback,
                      queue='pingqueue',
                      no_ack=True)

print(' [*] Waiting for ping back. To exit press CTRL+C')
channel.start_consuming()
