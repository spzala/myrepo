#!/usr/bin/env python
import pika

PASSWORD = 'ping_pong'
HOST = 'queue-rabbitmq.ping-pong.svc.cluster.local'
PORT = 5672
QUEUE = 'ping'
BALL = 'White'

credentials = pika.PlainCredentials('admin', PASSWORD)
parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)

print ("Connecting to queue at " + HOST)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.queue_declare(queue=QUEUE)

# Throw a ball
channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body=BALL)

connection.close()

print("Done throwing a ball")
