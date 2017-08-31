#!/usr/bin/env python
import pika
credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('my-release-rabbitmq.default.svc.cluster.local', 15672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
print("Ping")
connection.close()
