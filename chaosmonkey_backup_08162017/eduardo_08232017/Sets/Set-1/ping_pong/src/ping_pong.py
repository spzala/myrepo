#!/usr/bin/env python
import pika

PASSWORD = 'ping_pong'
HOST = 'queue-rabbitmq.ping-pong.svc.cluster.local'
PORT = 5672
QUEUE = 'ping'
OTHER_QUEUE = 'pong'
BALL = 'White'

def callback():
	print ("Received a ball")
	channel.basic_publish(exchange='',
                      routing_key=OTHER_QUEUE,
                      body=BALL)


credentials = pika.PlainCredentials('admin', PASSWORD)
parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)

print ("Connecting to queue at " + HOST)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue=QUEUE)

channel.basic_consume(callback,
    	                  queue=QUEUE,
        	              no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()
