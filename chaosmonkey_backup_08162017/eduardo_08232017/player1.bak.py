#!/usr/bin/env python
import pika
import time
import datetime

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('192.168.99.100', 32340, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.queue_declare(queue='pingqueue')
channel.queue_declare(queue='pongqueue')

#endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
t_end = time.time() + 10 * 1
while time.time() < t_end:
  print "while called"
  def callback(ch, method, properties, body):
    #print(" [x] Plaer 1 Received ping %r" % body)
    print("PongXXXXX")
    channel.basic_publish(exchange='',
                  	routing_key='pingqueue',
                  	body="Ping")
    #print("Sent ping on pingqueue")
    
  channel.basic_consume(callback,
                      	queue='pongqueue',
                      	no_ack=True)
  print(' [*] Waiting for ping back. To exit press CTRL+C')
  channel.start_consuming()
