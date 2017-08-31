#!/usr/bin/env python
import pika

# this queue is the destination queue
credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('192.168.99.100', 32340, '/', credentials)
connection = pika.BlockingConnection(parameters)
print " connection created"
